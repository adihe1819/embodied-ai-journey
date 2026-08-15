# embodied-ai-journey

我是何嘉乐，西南交通大学智能建造专业本科生。

这是我的综合学习仓库。Python 小练习、深度学习基础、画图、机器人感知和具身智能相关的尝试，都会先放在这里，所以内容会比较杂。

课程内容单独整理在 [cs61a-learning](https://github.com/adihe1819/cs61a-learning) 和 [cs231n-learning](https://github.com/adihe1819/cs231n-learning)，不放在这里。

## 目前在学

- Python、NumPy 和 Pandas
- PyTorch 基础和神经网络训练
- 计算机视觉、ROS 2 和机器人感知

## 仓库里的内容

- [`DNN.py`](DNN.py)：一个三分类的小练习，数据由程序生成，主要用来熟悉数据划分、训练循环和测试集评估。
- [`numpy_notes.py`](numpy_notes.py)：NumPy 的数组、切片、广播和矩阵运算练习。
- [`pandas_notes.py`](pandas_notes.py)：Pandas 的分箱、分组和透视表练习。
- [`matplotlibProject`](matplotlibProject)：用 Matplotlib 画二维波纹图。
- [`notes`](notes)：神经网络和 CNN 的学习笔记。
- [`learning-progress.md`](learning-progress.md)：最近在做什么，以及还没做完的内容。

## 运行

```bash
pip install -r requirements.txt

python numpy_notes.py
python pandas_notes.py
python matplotlibProject/matplot.py
```

运行 DNN 还需要安装 PyTorch：

```bash
python DNN.py --epochs 50
```

2026 年 8 月 15 日，我在自己的电脑上重新跑了一遍 `DNN.py`。使用的是 Python 3.12.4、PyTorch 2.11.0 和 RTX 5070 Ti Laptop GPU，训练 50 轮后的测试准确率是 99.42%。完整输出放在 [`results/dnn-run-2026-08-15.md`](results/dnn-run-2026-08-15.md)。

这里用的是简单的合成数据，结果只能说明代码和训练流程能够正常运行，不能代表真实图像任务的效果。

## 接下来想做的

- 做一个完整的 CNN 图像分类练习
- 继续学习 ROS 2，并尝试做一个机器人感知小项目
- 把零散的小实验和学习记录慢慢整理清楚

## 联系方式

- GitHub：[@adihe1819](https://github.com/adihe1819)
- Email：adihe1819@gmail.com
