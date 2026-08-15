# Embodied AI Learning Journey

> 何嘉乐的具身智能、机器人感知与深度学习基础记录。

这个仓库用于保存本科阶段的学习笔记、可运行的小实验和阶段复盘。这里会明确区分 **已验证**、**学习中** 与 **计划中**，不会把课程材料或尚未完成的实验包装成个人成果。

## 当前重点

- Python、NumPy、Pandas 与数据处理基础
- PyTorch 训练流程与模型评估
- 计算机视觉与 CNN 基础
- 机器人感知、ROS 2 与具身智能方向调研

## 当前可查看内容

| 内容 | 状态 | 说明 |
| --- | --- | --- |
| [NumPy 基础练习](numpy_notes.py) | 已整理 | 数组形状、索引、广播、聚合与矩阵乘法 |
| [Pandas 基础练习](pandas_notes.py) | 已整理 | DataFrame、分箱、分组和透视表 |
| [DNN 合成数据分类](DNN.py) | 代码已整理，待 PyTorch 环境验证 | 设计为自动选择 CPU/GPU 的三分类训练示例 |
| [神经网络训练流程](notes/neural-network-training-workflow.md) | 已整理 | 从数据划分到评估与常见错误 |
| [CNN 学习笔记](notes/cnn-learning-notes.md) | 学习中 | 当前为概念和实验清单，不包含虚构结果 |
| [Matplotlib 可视化](matplotlibProject/matplot.py) | 代码已整理，待环境复验 | 生成二维波纹热力图和 SVG 文件 |
| [具身智能学习路线图](AI+具身智能大学成长路线图.md) | 规划文档 | 只表示学习方向，不代表已掌握全部内容 |

## 仓库结构

```text
embodied-ai-journey/
├── README.md
├── requirements.txt
├── learning-progress.md
├── numpy_notes.py
├── pandas_notes.py
├── DNN.py
├── notes/
│   ├── neural-network-training-workflow.md
│   └── cnn-learning-notes.md
├── matplotlibProject/
│   ├── matplot.py
│   └── my_wave_plot.svg
└── AI+具身智能大学成长路线图.md
```

## 运行环境

基础练习：

```bash
pip install -r requirements.txt
python numpy_notes.py
python pandas_notes.py
python matplotlibProject/matplot.py
```

DNN 示例需要 PyTorch：

```bash
python DNN.py --epochs 50
```

脚本会自动选择 CUDA 或 CPU。仓库暂不提交数据集、模型权重和第三方课程讲义。

## 学习记录原则

1. 只把自己理解并复核过的内容标记为已完成。
2. 保存代码、运行方法、错误记录和结果，而不只罗列技术名词。
3. 第三方材料只提供来源说明，不直接上传受版权保护的讲义、安装包和课程答案。
4. AI 工具可用于结构整理和代码检查，但实验结果必须来自真实运行。

## 后续计划

- [ ] 为 DNN 示例补充真实损失曲线和准确率记录
- [ ] 完成一个 CNN 图像分类实验并记录混淆矩阵
- [ ] 补充 CS231n 公开课程的个人概念笔记
- [ ] 增加机器人感知或目标检测小实验
- [ ] 按周更新 `learning-progress.md`

## 联系方式

- GitHub: [adihe1819](https://github.com/adihe1819)
- Email: adihe1819@gmail.com
