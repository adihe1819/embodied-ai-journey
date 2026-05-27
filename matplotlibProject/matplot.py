#import matplotlib.pyplot as plt
#import numpy as np
#Fig1 = plt.figure() # 创建新图窗
#x = np.linspace(-2,2,5000) # 数据的 x 值
#y =x**3 # 数据的 y 值
#plt.plot(x,y,color='purple',marker='o')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('cubic curve')
#plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(-2, 2, 400)
#
# y1 = x**2
# y2 = x**3
# plt.grid(True)
# plt.plot(x, y1, label='x^2')
# plt.plot(x, y2, label='x^3')
# plt.axis('equal')
# ax = plt.gca()
# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
#
# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 10, 100)
#
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# plt.plot(x, y1, label='sin(x)')
# plt.plot(x, y2, label='cos(x)')
#
# plt.title("Multiple Curves")
# plt.xlabel("x")
# plt.ylabel("y")
#
# plt.legend()   # ⭐关键：显示图例
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 10, 200)
#
# plt.figure(figsize=(8,4))
#
# plt.plot(x, np.sin(x), label='sin')
# plt.plot(x, np.cos(x), label='cos')
# plt.plot(x, np.sin(x) + np.cos(x), label='sin+cos')
#
# plt.title("Multi-Curve Demo")
# plt.xlabel("x")
# plt.ylabel("y")
#
# plt.legend()
# plt.grid(True)
#
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x=np.linspace(0,1,100)
# fig, axes = plt.subplots(2,1)
# axes[0].plot(x,np.sin(x))
# axes[0].set_title("sin(x)")
#
# axes[1].plot(x, np.cos(x))
# axes[1].set_title("cos(x)")
# plt.tight_layout()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)
#
# # 坐标轴移到原点
# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
#
# # 刻度
# ax.set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
# ax.set_xticklabels([r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$'])
#plt.show()


# import matplotlib.pyplot as plt  # 导入Matplotlib的绘图模块，命名为plt，这是Python中标准的绘图核心工具箱
# import numpy as np  # 导入数值计算库NumPy，命名为np，用于高性能的矩阵运算和生成数据
#
# # 1. 生成基础的一维等差数列数据
# x = np.linspace(0, 10, 1000)  # 在0到10的区间内，均匀切分成1000个点，生成一个形状为 (1000,) 的一维向量
#
# # 2. 核心数学计算：通过NumPy广播机制强行从一维衍生出二维网格数据
# # np.sin(x) 形状是 (1000,)，代表横向信号
# # np.cos(x).reshape(-1, 1) 将cos(x)从一维强行重塑为 (1000, 1) 的纵向列向量
# # 一个行向量乘以一个列向量，底层会自动触发广播机制，像织网一样交叉相乘，生成一个 (1000, 1000) 的二维能量场矩阵
# y = np.sin(x) * np.cos(x).reshape(-1, 1)
#
# # 3. 实例化画布与子图（面向对象风格的标准初始化）
# # plt.subplots() 会同时返回两个对象：
# # fig 代表整张大画板（管理整体窗口、保存文件等操作）
# # ax 代表画板上的具体子图坐标轴（负责具体的数据绘制、刻度控制）
# fig, ax = plt.subplots()
#
# # 4. 调用imshow函数将二维矩阵渲染为“像素图像/热力图”
# # y: 传入的 (1000, 1000) 二维数据矩阵主体
# # extent=[0, 10, 0, 10]: 将默认的 [0~1000] 像素下标刻度，强制映射到真实的 [0~10] 物理坐标区间
# # origin='lower': 强行将图像零点(0,0)拉到左下角，符合标准数学笛卡尔坐标系的直觉（默认是在左上角）
# # cmap='viridis': 指定颜色映射表为“翠绿黄紫”色调，数值越小颜色越深（紫），数值越大颜色越亮（黄）
# ax.imshow(y, extent=[0, 10, 0, 10], origin='lower', cmap='viridis')
#
# # 5. 生产环境数据落盘：直接将当前画布保存到本地硬盘
# # "my_wave_plot.svg": 保存的文件名称
# # format="svg": 强制指定保存为SVG矢量图格式，保证图片无论怎么放大都绝对清晰、没有毛刺
# fig.savefig("my_wave_plot.svg", format="svg")
#
# # 6. 进程阻断与窗口唤醒
# # 显式通知操作系统唤起原生的图形GUI界面，弹出交互式绘图窗口展示图片。
# # 注意：在纯 .py 脚本中，此行必须写在最后，否则程序会直接静默结束，窗口无法保持显示
# plt.show()

import torch

