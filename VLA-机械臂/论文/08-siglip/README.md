# SigLIP

**2026-11-20 · 从 Spatial Forcing 的图 1 追读 SigLIP 原论文摘要和结论。** 这是为理解视觉编码器做的补读。

## 原文

*Sigmoid Loss for Language Image Pre-Training*，Xiaohua Zhai、Basil Mustafa、Alexander Kolesnikov、Lucas Beyer，ICCV 2023。选读摘要和 §5 结论。[CVF 会议页及全文](https://openaccess.thecvf.com/content/ICCV2023/html/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.html)

## 阅读注释

| 原文定位 | 我读到的意思 | 需要保留的条件 |
| --- | --- | --- |
| 摘要、§5 | 预训练的 sigmoid 损失在单个图文配对上计算，相比 softmax 对比损失，省去对整组相似度统一归一化的步骤。 | 这里读到的是图文预训练目标。论文的图文或图像分类实验使用各自的指标。 |
| [Spatial Forcing](../06-spatial-forcing/README.md) 图 1、§2.1 | 在 SF 对接的模型里，SigLIP 参与产生视觉编码。 | 区分图文预训练中的文本分支、部署时处理指令的文本 tokenizer，以及训练时提供几何特征的 VGGT。 |

## 个人思考

我从 SF 的架构图问起，图里的 Image Tokenizer 和 Text Tokenizer 各是谁？听到视觉侧用到 SigLIP 和 DINOv2 后，我选择先看 SigLIP，并要求回到原论文读摘要和结论。下次要追这条线，可以从 §2 跟一遍正负图文配对对应的损失。

[返回阅读档案](../../README.md)
