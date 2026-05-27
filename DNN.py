##生成数据集
import torch
# import torch.nn as nn
ts1=torch.rand(10000,1)
ts2=torch.rand(10000,1)
ts3=torch.rand(10000,1)
y1=((ts1+ts2+ts3)<1).float()
y2=(((ts1+ts2+ts3)>1) & ((ts1+ts2+ts3)<2)).float()
y3=((ts1+ts2+ts3)>2).float()
data=torch.cat((ts1,ts2,ts3,y1,y2,y3),axis=1)
data=data.to("cuda:0")
print(data.shape)
train_size=int(len(data)*0.7)
test_size=len(data)-train_size
data=data[torch.randperm(data.size(0))]
train_data=data[:train_size,:]
test_data=data[train_size:,:]
##构建模型
import torch.nn as nn
class DNN(nn.Module):
 def __init__(self):
    super(DNN,self).__init__() 
    self.net=nn.Sequential(
      nn.Linear(3,64),nn.ReLU(),
        nn.Linear(64,128),nn.ReLU(),
        nn.Linear(128,64),nn.ReLU(),
        nn.Linear(64,3)
    )
def forward(self,x):
  y=self.net(x)
  return y
model=DNN().to("cuda:0")
for name, param in model.named_parameters():
 print(f"参数:{name}\n 形状:{param.shape}\n 数值:{param}\n")