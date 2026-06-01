# ##生成数据集
# import torch
# # import torch.nn as nn
# ts1=torch.rand(10000,1)
# ts2=torch.rand(10000,1)
# ts3=torch.rand(10000,1)
# y1=((ts1+ts2+ts3)<1).float()
# y2=(((ts1+ts2+ts3)>1) & ((ts1+ts2+ts3)<2)).float()
# y3=((ts1+ts2+ts3)>2).float()
# data=torch.cat((ts1,ts2,ts3,y1,y2,y3),axis=1)
# data=data.to("cuda:0")
# print(data.shape)
# train_size=int(len(data)*0.7)
# test_size=len(data)-train_size
# data=data[torch.randperm(data.size(0))]
# train_data=data[:train_size,:]
# test_data=data[train_size:,:]
# ##构建模型
# import torch.nn as nn
# class DNN(nn.Module):
#  def __init__(self):
#     super(DNN,self).__init__() 
#     self.net=nn.Sequential(
#       nn.Linear(3,64),nn.ReLU(),
#         nn.Linear(64,128),nn.ReLU(),
#         nn.Linear(128,64),nn.ReLU(),
#         nn.Linear(64,3)
#     )
# def forward(self,x):
#   y=self.net(x)
#   return y
# model=DNN().to("cuda:0")
# for name, param in model.named_parameters():
#  print(f"参数:{name}\n 形状:{param.shape}\n 数值:{param}\n")

#批量梯度下降
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
df=pd.read_csv("data.csv",index_col=0)
arr=df.values
arr=arr.astype(np.float32)
ts=torch.tensor(arr)
ts=ts.to("cuda:0")
train_size=int(len(ts)*0.7)
test_size=len(ts)-train_size
ts=ts[torch.randperm(ts.size(0))]
train_data=ts[:train_size,:]
test_data=ts[train_size:,:]
class DNN(nn.Module):
 def __init__(self):
    super(DNN,self).__init__() 
    self.net=nn.Sequential(
      nn.Linear(8,32),nn.Sigmoid(),
        nn.Linear(32,8),nn.Sigmoid(),
        nn.Linear(8,4),nn.Sigmoid(),
        nn.Linear(4,1),nn.Sigmoid()
    )
 def forward(self,x):
  y=self.net(x)
  return y
model=DNN().to("cuda:0")
loss_fn=nn.BCELoss(reduction="mean")
learning_rate=0.005
optimizer=torch.optim.Adam(model.parameters(),lr=learning_rate)
epochs=5000
losses=[]
X=train_data[:, :-1]
Y=train_data[:, -1].reshape((-1, 1))
for epoch in range(epochs):
    pred=model(X)
    loss=loss_fn(pred,Y)
    losses.append(loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
   
Fig=plt.figure()
plt.plot(range(epochs),losses)
plt.ylabel("loss")
plt.xlabel("epoch")
print("\n====== 测试集效果评估 ======")
X_test = test_data[:, :-1]   # 前 8 列为测试输入特征
Y_test = test_data[:, -1].reshape((-1, 1))  # 最后 1 列为真实输出标签

# 2. 绝对防御：关闭梯度计算，不建立计算图，省显存且速度极快
with torch.no_grad():
    Pred = model(X_test)  # 盲猜测试集答案
    
    # 二分类门槛：大于等于 0.5 的认为它是分类 1，小于 0.5 的认为它是分类 0
    Pred[Pred >= 0.5] = 1
    Pred[Pred < 0.5] = 0
    
    # 算算答对了多少题
    correct = torch.sum((Pred == Y_test).all(1))
    total = Y_test.size(0)  # 总共的考试样本数
    
    print(f'测试集精准度: {100 * correct / total:.6f} %')

# 3. 最后大收网，把图弹出来
plt.show()

# # 1. 题库切片：前 8 列是输入特征，最后一列（第9列）是真实答案
# X_train = train_data[:, :8]
# Y_train = train_data[:, 8:]

# # 2. 引入教练和更新策略
# criterion = nn.MSELoss()  # 损失函数：均方误差，用来算模型“现在有多笨”
# optimizer = torch.optim.Adam(model.parameters(), lr=0.01)  #
# epochs = 1000
# losses = []  # 拿个小本本，记录每轮的 loss 变动，方便待会儿画瀑布图

# print("开始训练，模型正在玩命下山中...")

# for epoch in range(epochs):
#     # 1. 前向传播：模型根据 8 列特征，盲猜一个输出结果
#     pred = model(X_train)
    
#     # 2. 算误差：看看这次猜得离真实答案 Y 差了多远
#     loss = criterion(pred, Y_train)
#     losses.append(loss.item())  # 剥离成纯数字记下来，防止计算图塞爆显存
    
#     # 3. 三位一体梯度更新更新
#     optimizer.zero_grad()  # 清垃圾：把上一轮的残余梯度账本撕掉
#     loss.backward()        # 找方向：顺藤摸瓜，用计算图算出每个参数该怎么改
#     optimizer.step()       # 迈大步：Adam 依据方向，真正修改 weight 和 bias
    
#     # 每隔 100 轮在控制台吼一声，让你肉眼监控进度
#     if (epoch + 1) % 100 == 0:
#         print(f"第 {epoch+1}/{epochs} 轮迭代完成 | 当前笨拙度 (Loss): {loss.item():.6f}")
#         print("训练全部结束！正在生成可视化收敛大图...")

# # 激活 Matplotlib 画布
# plt.figure(figsize=(8, 5))
# plt.plot(range(epochs), losses, color="royalblue", linewidth=2)
# plt.xlabel("Epochs (迭代轮数)")
# plt.ylabel("Loss (有多笨)")
# plt.title("Model Training Convergence (模型收敛曲线)")
# plt.grid(True, linestyle="--", alpha=0.5)  # 加上之前学到的高档淡色网格

# plt.show()  # 彻底阻断，在 VSCode 里弹出独立高清图表窗口！