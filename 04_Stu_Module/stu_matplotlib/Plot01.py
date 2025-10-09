"""绘制一个正弦波"""

import numpy as np
import matplotlib.pyplot as plt

# 创建x值，范围从-π到π，步长为0.01，覆盖一个周期
x = np.linspace(-np.pi, np.pi, 1000)

# 计算对应的y值，即sin(x)
y = np.sin(x)

# 创建图形并设置坐标轴
fig, ax = plt.subplots()
ax.set_xlim([-np.pi, np.pi])  # 设置x轴范围
ax.set_ylim([-1, 1])  # 设置y轴范围
ax.set_xlabel('x')  # x轴标签
ax.set_ylabel('sin(x)')  # y轴标签
ax.set_title('y = sin(x) in one period')  # 图像标题

# 绘制sin(x)函数
plt.plot(x, y)

# 显示图像
plt.show()
