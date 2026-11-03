# 6-DOF GraspNet

**2026-10-27 至 10-30 · 精读中。** 已读题目、摘要、引言和结论，梳理了图 1–11、真机表 1，以及覆盖率和梯度优化。10 月 30 日提出接着读第 3 节，采样器、评估器和优化公式的逐节阅读待续。

## 原文

*6-DOF GraspNet: Variational Grasp Generation for Object Manipulation*，Arsalan Mousavian、Clemens Eppner、Dieter Fox，ICCV 2019。正文第 1–2 页介绍抓取任务与多候选的动机，第 3–5 页讲位姿生成，第 6–8 页是评估、真机结果和结论。[会议版 PDF](https://openaccess.thecvf.com/content_ICCV_2019/papers/Mousavian_6-DOF_GraspNet_Variational_Grasp_Generation_for_Object_Manipulation_ICCV_2019_paper.pdf) · [作者机构页面](https://research.nvidia.com/labs/srl/publication/mousavian-20196-dof/)

## 阅读注释

**从一帧深度图到一组抓法。** 图 3 的信息流是目标物体的局部点云 → 条件 VAE 采样抓取位姿 → 评估器打分 → 用评估器对位姿的梯度继续优化。位姿包含夹爪的位置与朝向。图 2 展示同一个杯子如何产生多种候选，再由后续规划筛掉碰撞或运动学不可达的候选。图中的颜色表示评估分数，真机结果单独记录在表 1。[会议版 PDF，图 2–3 与表 1](https://openaccess.thecvf.com/content_ICCV_2019/papers/Mousavian_6-DOF_GraspNet_Variational_Grasp_Generation_for_Object_Manipulation_ICCV_2019_paper.pdf)

**从候选优化读到实时反馈。** 图 5 的一串夹爪显示同一个候选在优化迭代中如何移动。输入仍是计算所用的物体点云，更新的是候选位姿变量。第 5 节把评估器用于真实机械臂接近物体时的实时反馈列为后续方向。若实现这个闭环，机械臂运动后需再获取观测、更新候选并交给控制或规划模块执行，再进入下一次反馈。[会议版 PDF，图 5 与第 5 节](https://openaccess.thecvf.com/content_ICCV_2019/papers/Mousavian_6-DOF_GraspNet_Variational_Grasp_Generation_for_Object_Manipulation_ICCV_2019_paper.pdf)

**覆盖率与成功率的分母。** 论文第 6 页的参考集来自仿真采样与成功验证，是连续抓取空间的一组样本。覆盖率统计其中有多少参考位姿的平移位置邻近模型候选，公开实现的半径为 `0.02 m`。同一个参考位姿即使匹配多个候选，也只记一次。成功率统计被评测的模型抓取中有多少成功。仿真曲线沿着候选评分阈值变化计算这两个量。示意例子中，20 个模型候选里有 18 个成功，同时覆盖 100 个参考抓法中的 30 个，成功率是 90%，覆盖率是 30%。有限采样容易集中到同一片位置，图 9 检查了扩大采样量对覆盖率的影响。作者在另一组真机实验中报告了 88% 的总体抓取成功率。[会议版 PDF，第 6–8 页](https://openaccess.thecvf.com/content_ICCV_2019/papers/Mousavian_6-DOF_GraspNet_Variational_Grasp_Generation_for_Object_Manipulation_ICCV_2019_paper.pdf) · [公开评测代码](https://github.com/NVlabs/6dof-graspnet/blob/cd08b6c559e51a187ab65faea6415f51239808b8/eval.py#L366)

### 图表索引

| 定位 | 阅读时记录的内容 |
| --- | --- |
| 图 1–2，第 1–2 页 | Panda 机械臂与多样抓法。杯子场景的最终候选还受运动学和碰撞约束。 |
| 图 3–4，第 4 页 | 图 3 连接点云、采样、评估与优化。图 4 展开训练时抓取位姿经编码器进入潜空间、再由条件解码器重建的过程。 |
| 图 5–6，第 5–6 页 | 图 5 看候选在优化中的变化。图 6 看仿真生成的成功抓取如何分布在碗和盒子周围。 |
| 图 7–9，第 7 页 | 分别检验潜空间维度、优化迭代次数、采样量与采样方式。结合成功率和覆盖率读曲线。 |
| 图 10–11、表 1，第 8 页 | 图 10 展示用于真机测试的物体姿态。图 11 对比杯子的候选分布。表 1 给出实际抓取结果。 |

## 个人思考

据 10 月 27–30 日精读对话和我的 Pass 1 手写笔记整理。

- 我在笔记里把旧的规则或几何采样流程和本文放在一起，画出「点云 → 候选 → 评估 → 优化 → 外部规划筛选」这条线，并记下为什么需要多种抓法。
- 读到结论时，我追问了一个具体矛盾。既然评估器已经用梯度把采样出的位姿往成功抓法推，作者为什么还把“引导接近中的机械臂”留作后续工作？我在笔记里把相机反馈、实时调整位姿放在未来方向一栏，和前面的候选优化分开记。
- 我最初把覆盖率的参考集理解成仿真找到的全部成功抓法，还把模型候选和真机运行联系在一起，因此接着问“为什么覆盖率不会是 100%”。这一问对应上面的两组样本和两套分母。

[返回阅读档案](../../README.md)
