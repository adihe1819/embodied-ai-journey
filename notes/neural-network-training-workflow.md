# 神经网络训练流程笔记

这份笔记由个人原始总结整理而来，补充了验证集、数据泄漏、模型模式切换和不同分类损失函数的区别。

## 1. 明确任务与评价指标

先判断任务类型，再选择输出形式、损失函数和指标：

| 任务 | 模型输出 | 常用损失 | 常用指标 |
| --- | --- | --- | --- |
| 二分类 | 一个原始 logit | `BCEWithLogitsLoss` | accuracy、precision、recall、F1 |
| 多分类 | 每类一个 logit | `CrossEntropyLoss` | accuracy、混淆矩阵 |
| 回归 | 连续值 | `MSELoss` / `L1Loss` | MAE、RMSE |

`BCEWithLogitsLoss` 已经包含 Sigmoid，训练时不要在模型输出层重复添加 Sigmoid。`CrossEntropyLoss` 接收未经 Softmax 的 logits，标签应为整数类别编号。

## 2. 准备数据

1. 读取或生成数据。
2. 检查缺失值、异常值、标签分布和重复样本。
3. 将连续特征转换为合适的浮点类型，例如 `float32`。
4. 先划分训练集、验证集和测试集，再根据训练集拟合归一化参数，避免数据泄漏。
5. 使用 `Dataset` 和 `DataLoader` 组织 mini-batch。

常见划分方式是 70%/15%/15% 或 80%/10%/10%，但小数据集还需要考虑交叉验证与分层抽样。

## 3. 定义模型

PyTorch 模型通常继承 `nn.Module`：

```python
class Classifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(8, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
        )

    def forward(self, x):
        return self.net(x)
```

输出层是否添加激活函数，应与损失函数配套，而不是机械套用 Sigmoid 或 Softmax。

## 4. 训练循环

每个 mini-batch 的核心顺序：

```python
model.train()
for features, labels in train_loader:
    logits = model(features)       # forward
    loss = loss_fn(logits, labels) # compute loss
    optimizer.zero_grad()          # clear old gradients
    loss.backward()                # backpropagation
    optimizer.step()               # update parameters
```

梯度默认会累积，因此需要在每次参数更新前清空旧梯度。

## 5. 验证与测试

验证和测试阶段需要关闭训练特性和梯度记录：

```python
model.eval()
with torch.no_grad():
    predictions = model(features)
```

- 验证集用于选择超参数、训练轮数和最佳模型。
- 测试集只用于最终评估，不应反复参与调参。
- 除总体准确率外，应检查类别不平衡、混淆矩阵和失败样本。

## 6. 训练监控

建议至少记录：

- 每轮训练损失与验证损失；
- 训练集与验证集指标；
- 学习率；
- 随机种子、环境、数据版本和模型配置；
- 最佳 checkpoint 对应的轮次。

训练损失继续下降、验证损失反而上升，通常提示过拟合。两者都很高，则可能是欠拟合、特征不足或训练配置不合适。

## 7. 常见错误

- `BCELoss` 与原始 logits 直接搭配；更稳妥的做法是使用 `BCEWithLogitsLoss`。
- `CrossEntropyLoss` 前手动执行 Softmax。
- 训练、验证、测试数据发生交叉或归一化统计量泄漏。
- 训练时忘记 `model.train()`，测试时忘记 `model.eval()`。
- 代码写死为 `cuda:0`，导致没有 GPU 时无法运行。
- 只报告最好的一次准确率，不保存随机种子和完整配置。
- 使用测试集反复调参，导致最终指标失真。

## 8. 下一步实践

当前仓库的 `DNN.py` 用合成数据展示了完整训练流程。下一步将增加：

- 损失曲线；
- 混淆矩阵；
- 不同激活函数与学习率的对比；
- 一个真实图像分类数据集上的 CNN 实验。

