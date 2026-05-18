#import pandas as pd
#import torch
#v=torch.tensor([0,0.25,0.5,0.75,1])#创建一个 PyTorch 张量 v，包含五个值：0、0.25、0.5、0.75 和 1
#k=["a","b","c","d","e"]#创建一个列表 k，包含字符串 "a" 到 "e"
#sr=pd.Series(v,index=k)##创建一个 Series 对象，数据为 v，索引为 k
#print(sr)

#import pandas as pd
#v1=["似了",26,29,19]
##sr1=pd.Series(v1,index=i)
#v2=["海岛奇兵","欧尼","小镇娃","王朝"]
#sr2=pd.Series(v2,index=i)
#df=pd.DataFrame({"年龄":sr1,"身份":sr2})
#print(df)
#import pandas as pd
#v=[["似了","海岛奇兵"],[26,"欧尼"],[29,"小镇娃"],[19,"王朝"]]
#i=["蒋介石","柳智敏","asen","donk"]
#c=["身份","年龄"]
#df=pd.DataFrame(v,index=i,columns=c)
#print(df)

#import pandas as pd
#v=[55,11,22,33,44]
#k=["1","2","3","4","5"]
#sr=pd.Series(v,index=k)
#print(sr)
#print(sr["1":"3"])
#cut=sr["1":"3"]
#cut["1"]=100
#print(sr)

#import pandas as pd
#v1=[1,2,3,4,5]
#v2=[5,6,7]
#k1=["一号","二号","三号","四号","五号"]
#k2=["五号","六号","七号"]
#sr1=pd.Series(v1,index=k1)
#sr2=pd.Series(v2,index=k2)
#sr3=pd.concat([sr1,sr2])
#print(sr3)
#print(sr3.index)
#print(sr3.is_unique)

#import pandas as pd
#v1=[6,66,666]
#v2=["g","b","b"]
#sr1=pd.Series(v1,index=["一","二","三"])
#sr2=pd.Series(v2,index=["一","二","三"])
#df=pd.DataFrame({"评分":sr1,"字母":sr2})
#df.loc["四"]="6666","g"
#df["地区"]=["北京","上海","广州","深圳"]
#print(df)

#import pandas as pd
#v=[53,None,22,33,44]
#k=["first","second","third","fourth","fifth"]
#sr=pd.Series(v,index=k) 
#sr.dropna(how="all",inplace=True) # inplace=True 直接修改原 DataFrame  
#print(sr)

import pandas as pd

# 让 pandas 把中文字符按两倍宽度显示，解决列对齐问题

# 1. 核心函数：pd.read_excel
# 建议加上 index_col=0，把你表格的第一列（比如序号、工号）直接锁定为行标签
df = pd.read_excel(r"C:\Users\12836\Desktop\python\泰坦尼克.xlsx", index_col=0)

# 2. 肌肉记忆：用我们刚刚学的 head() 预览前 5 行，防止终端被刷屏

# 3. 顺便看一眼这个表格的物理形状（多少行，多少
age=pd.cut(df["年龄"],[0,18,120])
df.pivot_table("是否生还", index="性别")
fare=pd.qcut(df["费用"],3)
DF=df.pivot_table("是否生还", columns=["性别",age],index=["船舱等级",fare])
print(DF)