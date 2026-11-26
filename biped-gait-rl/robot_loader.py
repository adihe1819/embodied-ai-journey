"""双足模型加载与真碰撞网格净空计算工具。

运行前请通过环境变量 BIPED_SIM_DIR 指定团队仓库 kdwbll/Biped_Robot 的 simulation 目录路径
（例如：set BIPED_SIM_DIR=C:\\path\\to\\Biped_Robot\\simulation），或在 replay_gait_v8.py 中传入 --sim-dir。
"""
import os
import sys
from dataclasses import replace
from pathlib import Path

import numpy as np

MODEL_XML = "diagnostic_post_shaft_fix_gear_phase_25.xml"


def resolve_sim_dir(sim_dir=None) -> Path:
    cand = sim_dir or os.environ.get("BIPED_SIM_DIR")
    if cand:
        p = Path(cand).resolve()
        if (p / MODEL_XML).is_file():
            return p
        raise FileNotFoundError(f"在 {p} 中找不到模型文件 {MODEL_XML}")
    # 自动探测常见同级目录
    here = Path(__file__).resolve().parent
    for probe in [here.parent / "Biped_Robot" / "simulation", here.parent.parent / "Biped_Robot" / "simulation"]:
        if (probe / MODEL_XML).is_file():
            return probe
    raise FileNotFoundError(
        "未找到团队仓库 kdwbll/Biped_Robot 的 simulation 目录。"
        "请先 clone https://github.com/kdwbll/Biped_Robot 并设置环境变量 BIPED_SIM_DIR=<path>/Biped_Robot/simulation，"
        "或在运行脚本时传入 --sim-dir <path>/Biped_Robot/simulation。"
    )


SIM_DIR = None
_mujoco = None
_ServoSpec = None
_CandidateStandingServo = None


def _ensure_loaded(sim_dir=None):
    global SIM_DIR, _mujoco, _ServoSpec, _CandidateStandingServo
    if SIM_DIR is None or sim_dir is not None:
        SIM_DIR = resolve_sim_dir(sim_dir)
    os.chdir(SIM_DIR)
    if str(SIM_DIR) not in sys.path:
        sys.path.insert(0, str(SIM_DIR))
    if _mujoco is None:
        import mujoco
        from theoretical_servo import ServoSpec
        from candidate_standing_servo import CandidateStandingServo

        _mujoco = mujoco
        _ServoSpec = ServoSpec
        _CandidateStandingServo = CandidateStandingServo


SERVO_NAMES = [
    "左腿上舵机 L0_upper",
    "左腿下舵机 L0_knee",
    "右腿上舵机 L1_upper",
    "右腿下舵机 L1_knee",
    "中央转向舵机 hip",
]
FOOT_BODIES = ["L0_part6", "L1_part6"]
FOOT_MESH_GEOMS = ("L0_visual6", "L1_visual6")
TORSO_BODY = "robot_free"
CENTER_US = 1500.0


def foot_mesh_hull_verts(model):
    """提取 L0_visual6 / L1_visual6 实际地面碰撞网格的凸包顶点（最低点 z 与全网格数学严格一致）。"""
    gids = [model.geom(name).id for name in FOOT_MESH_GEOMS]
    hull_verts = []
    for gid in gids:
        mid = int(model.geom_dataid[gid])
        adr = int(model.mesh_vertadr[mid])
        num = int(model.mesh_vertnum[mid])
        all_v = model.mesh_vert[adr : adr + num]
        gadr = int(model.mesh_graphadr[mid])
        if gadr >= 0:
            n_hull = int(model.mesh_graph[gadr])
            hull_idx = model.mesh_graph[gadr + 2 + n_hull : gadr + 2 + 2 * n_hull]
            hull_verts.append(np.ascontiguousarray(all_v[hull_idx], dtype=np.float32))
        else:
            hull_verts.append(np.ascontiguousarray(all_v, dtype=np.float32))
    return gids, hull_verts


def foot_true_clearance_m(data, mesh_gids, hull_verts):
    """计算左右脚实际碰撞网格最低顶点当前离地高度（米，>= 0）。"""
    out = np.empty(2, dtype=np.float64)
    for leg, (gid, verts) in enumerate(zip(mesh_gids, hull_verts)):
        pos_z = float(data.geom_xpos[gid, 2])
        rot_z = data.geom_xmat[gid].reshape(3, 3)[2, :]
        z_min = pos_z + float(np.min(verts @ rot_z))
        out[leg] = max(0.0, z_min)
    return out


def load(hang=False, hang_height=0.10, sim_dir=None):
    _ensure_loaded(sim_dir)
    mujoco = _mujoco
    if not hang:
        model = mujoco.MjModel.from_xml_path(MODEL_XML)
        data = mujoco.MjData(model)
        mujoco.mj_resetDataKeyframe(model, data, 0)
    else:
        key_qpos = mujoco.MjModel.from_xml_path(MODEL_XML).key_qpos[0].copy()
        spec = mujoco.MjSpec.from_file(MODEL_XML)
        torso = spec.body(TORSO_BODY)
        spec.delete(torso.joints[0])
        torso.pos = [key_qpos[0], key_qpos[1], key_qpos[2] + hang_height]
        torso.quat = key_qpos[3:7]
        for key in list(spec.keys):
            spec.delete(key)
        model = spec.compile()
        data = mujoco.MjData(model)
        data.qpos[:] = key_qpos[7:]
    mujoco.mj_forward(model, data)
    return model, data


def make_servo(model, data):
    _ensure_loaded()
    return _CandidateStandingServo(model, data, replace(_ServoSpec(), kp_nm_per_rad=4.0), ki=1.5)


def torso_tilt_deg(data):
    z_axis_z = data.body(TORSO_BODY).xmat[8]
    return float(np.degrees(np.arccos(np.clip(z_axis_z, -1.0, 1.0))))


def foot_forces(model, data):
    _ensure_loaded()
    mujoco = _mujoco
    foot_ids = [model.body(name).id for name in FOOT_BODIES]
    forces = [0.0, 0.0]
    f6 = np.zeros(6)
    for i in range(data.ncon):
        c = data.contact[i]
        b1, b2 = model.geom_bodyid[c.geom1], model.geom_bodyid[c.geom2]
        if 0 not in (b1, b2):
            continue
        other = b2 if b1 == 0 else b1
        if other in foot_ids:
            mujoco.mj_contactForce(model, data, i, f6)
            forces[foot_ids.index(other)] += f6[0]
    return forces
