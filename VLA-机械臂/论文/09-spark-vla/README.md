# SPARK-VLA

**2026-11-21 · 开始读标题与摘要。** 下次可从 §1 引言和方法总览图继续。

## 原文

*Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models*，Jungin Park、Chaoran Zhu、Changjae Oh、Kwanghoon Sohn。阅读使用 2026 年 11 月 7 日的 arXiv v1。[论文摘要](https://arxiv.org/abs/2611.10443v1) · [PDF](https://arxiv.org/pdf/2611.10443v1)

## 阅读注释

| 原文定位 | 我读到的意思 | 需要保留的条件 |
| --- | --- | --- |
| 摘要 | 原有视觉通路保留。另一个带 LoRA 的视觉通路通过注意力响应蒸馏学习几何知识。 | 三维专家提供训练监督。部署时策略运行学习后的视觉通路和路由。 |
| 摘要 | 知识路由选择对动作预测有用的视觉 token。作者借助动作损失的梯度构造路由监督。 | 这一轮读到思路，路由目标怎样计算和选择仍待方法节核对。 |

## 个人思考

我为 SPARK-VLA 单独开了阅读对话，从标题和摘要开始。之前在 SF 上问的是几何知识怎样学进去。读完这篇摘要后，下一步可以顺着这个问题查，它怎样同时保留原有视觉信息和新学到的空间信息。

[返回阅读档案](../../README.md)
