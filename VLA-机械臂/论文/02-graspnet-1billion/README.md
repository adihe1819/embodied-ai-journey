# GraspNet-1Billion

**2026-10-29 至 10-30 · 已完成第一轮框架梳理。** 读了题目、摘要、引言、结论、图 1–6、表 1–4 和第 5 节实验。数据集构建与模型训练的正文细节和公式待继续读。

## 原文

*GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping*，Hao-Shu Fang、Chenxi Wang、Minghao Gou、Cewu Lu，CVPR 2020。引言见正文第 1–2 页，图 5 在 PDF 第 6 页，实验和结论在第 7–8 页。[会议版 PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf) · [项目主页](https://graspnet.net/)

## 阅读注释

**数据与评测。** 作者采集了 190 个杂乱场景的 97,280 幅 RGB-D 图像，涉及 88 个物体。在单个物体网格上先计算抓取，再借助场景中的物体位姿把抓取转换到场景坐标系并做碰撞检查。超过十亿是抓取位姿标注的数量。评测基于解析抓取质量判定，可以评估模型提出的新位姿，按排序后的预测结果和摩擦条件计算 AP。[会议版 PDF，第 3 节与图 1–3](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf)

**图 5 的 `M×(3+C)`。** 输入是场景点云 `N×3`。点云编码器采样保留 `M` 个点，每点的记录由 3 个坐标值与 `C` 个几何特征组成。ApproachNet 给抓取点和候选接近方向打分，随后沿选定方向取圆柱邻域并转入局部坐标系。OperationNet 估计抓取操作参数与质量，ToleranceNet 估计抓法对扰动的容忍程度。[会议版 PDF，第 4 节与图 5](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf)

**表 4 的分类与回归。** 预设接近方向或旋转角度档位，可以先给各档评分，再选档位并处理残差。直接回归的对照方案直接预测连续方向和角度。自回归描述另一个维度，即生成的后一步使用前面已生成的输出。表 4 的对照改变了抓取参数的预测形式。在 Kinect 已见物体组，完整模型的 AP 为 29.88，改为直接回归为 23.74，移除 ToleranceNet 为 28.53。[会议版 PDF，§5.3 与表 4](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf)

### 图表索引

| 定位 | 阅读时记录的内容 |
| --- | --- |
| 图 1–3 | 真实场景采集、物体级抓取库、坐标变换与场景碰撞检查。图 2 把数据、标注和评测放在一起。 |
| 图 4–6 | 图 4 定义夹爪的接近方向、距离、旋转和开口宽度。图 5 展开网络流程，图 6 展示预测抓法。 |
| 表 1–2 | 表 1 比较数据集。表 2 验证解析抓取标注在真机上的表现，最高评分组平均成功率约 96%。 |
| 表 3–4 | 表 3 比较模型在 Seen、Unseen but Similar 和 Novel 上的基准 AP。表 4 比较参数预测形式与 ToleranceNet 的作用。 |

## 个人思考

据 10 月 29–30 日精读对话和我的 Pass 1 手写笔记整理。

- 我在笔记里先把论文拆成三项贡献，分别是数据集、统一评测和端到端抓取位姿网络。我在自己画的网络流程旁边记下了与 6-DOF GraspNet 的联系，疑问集中在两篇怎样拆解抓取问题。
- 看图 5 时，我停下来问“为什么这个图里是 `M(C+3)`”。随后又请对话按图 5 展开网络的数据流。
- 读消融表时，我已经辨认出 ApproachNet 和 OperationNet，接着把 regression 和自回归联在了一起，于是追问“分类预测替换为直接回归”到底换了什么。

[返回阅读档案](../../README.md)
