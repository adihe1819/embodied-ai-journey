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
| [NumPy 基础练习](numpy_notes.py) | 已运行验证 | 数组形状、索引、广播、聚合与矩阵乘法 |
| [Pandas 基础练习](pandas_notes.py) | 已运行验证 | DataFrame、分箱、分组和透视表 |
| [DNN 合成数据分类](DNN.py) | 已运行验证 | CUDA 训练 50 轮，测试准确率 99.42% |
| [神经网络训练流程](notes/neural-network-training-workflow.md) | 已整理 | 从数据划分到评估与常见错误 |
| [CNN 学习笔记](notes/cnn-learning-notes.md) | 学习中 | 当前为概念和实验清单，不包含虚构结果 |
| [Matplotlib 可视化](matplotlibProject/matplot.py) | 已运行验证 | 生成二维波纹热力图和 SVG 文件 |
| [DNN 运行记录](results/dnn-run-2026-08-15.md) | 已记录 | 保存实际环境、训练日志与结果说明 |
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
├── results/
│   └── dnn-run-2026-08-15.md
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

## 已验证环境与结果

- 2026-08-15 在 VS Code 中使用 Python 3.12.4 与 PyTorch 2.11.0 运行。
- DNN 自动选择 `NVIDIA GeForce RTX 5070 Ti Laptop GPU`，50 轮后测试准确率为 `99.42%`。
- NumPy、Pandas 与 Matplotlib 示例均运行结束；Matplotlib 已重新生成 SVG。
- 详细日志见 [DNN 运行记录](results/dnn-run-2026-08-15.md)。

## 后续计划

- [x] 为 DNN 示例补充真实训练日志和准确率记录
- [ ] 为 DNN 示例增加损失曲线
- [ ] 完成一个 CNN 图像分类实验并记录混淆矩阵
- [ ] 补充 CS231n 公开课程的个人概念笔记
- [ ] 增加机器人感知或目标检测小实验
- [ ] 按周更新 `learning-progress.md`

## 联系方式

- GitHub: [adihe1819](https://github.com/adihe1819)
- Email: adihe1819@gmail.com
