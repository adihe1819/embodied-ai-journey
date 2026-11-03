# ManipLLM

**2026-10-30 · 已读题目和摘要。** 本页记录首轮入口。引言、方法和实验的精读待续。

## 原文

*ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation*，Xiaoqi Li、Mingxu Zhang、Yiran Geng、Haoran Geng、Yuxing Long、Yan Shen、Renrui Zhang、Jiaming Liu、Hao Dong，CVPR 2024。已读部分位于正式版 PDF 第 1 页。[会议页](https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html) · [预印本全文入口](https://arxiv.org/abs/2312.16217)

## 阅读注释

**“以物体为中心”的操作。** 摘要从接触点和末端执行器方向切入。以掀锅盖为例，模型需要结合物体结构、可操作部位和语言要求来推断应当在哪里接触，以及夹爪从什么方向接近。这是阅读时用来理解题目的例子。[论文摘要](https://arxiv.org/abs/2312.16217)

**接触前后的处理。** 摘要描述的前段以 RGB 图像和文本提示为输入，利用多模态大语言模型预测末端位姿。初始接触建立后，主动阻抗适应策略在闭环中规划后续路点。作者还提出测试时适应，以匹配实际场景配置。这里记录的是摘要里的方法框架，具体的训练目标、控制反馈和实验条件留在方法与实验正文中核对。[论文摘要](https://arxiv.org/abs/2312.16217)

## 个人思考

10 月 30 日，我在对话里选择沿用此前的顺序，从题目和摘要开始读。现有讨论到这里为止，后面从引言和方法接着记录。

[返回阅读档案](../../README.md)
