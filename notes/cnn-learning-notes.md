# CNN 学习笔记（进行中）

> 当前状态：概念整理完成，独立训练实验和结果图尚未补充。

## 1. 为什么使用卷积

全连接网络把图像铺平成向量，会丢失二维空间结构，并产生大量参数。卷积层通过局部连接和参数共享提取边缘、纹理与更高层语义特征。

对于输入 `N x C_in x H x W`，二维卷积层通常输出：

```text
N x C_out x H_out x W_out
```

单个空间维度的输出大小为：

```text
floor((input + 2 * padding - dilation * (kernel - 1) - 1) / stride + 1)
```

## 2. 需要掌握的组件

- `Conv2d`：学习局部特征；
- ReLU：引入非线性；
- Max/Avg Pooling：压缩空间尺寸；
- Batch Normalization：改善训练稳定性；
- Dropout：缓解部分过拟合；
- Flatten / Global Average Pooling：连接卷积特征与分类头；
- Cross Entropy：多分类常用损失。

## 3. 目前能够解释的概念

- 通道数、卷积核大小、步幅和填充如何影响输出形状；
- 参数共享为什么比全连接层更适合图像；
- 训练模式与评估模式的区别；
- logits、Softmax 与 `CrossEntropyLoss` 的关系。

## 4. 尚未完成的实验

- [ ] 在公开图像数据集上训练一个基础 CNN；
- [ ] 保存训练/验证损失曲线；
- [ ] 输出混淆矩阵和失败样本；
- [ ] 比较 MLP 与 CNN；
- [ ] 记录 batch size、学习率和数据增强的影响；
- [ ] 对照 CS231n 笔记解释反向传播与正则化。

完成实验前，本文件不会填写准确率或声称模型已经跑通。

