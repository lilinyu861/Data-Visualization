import numpy as np
from matplotlib import pyplot as plt


# 基础柱状图
data = [1, 3, 2, 4]
labels = ['a', 'b', 'c', 'd']
plt.bar(range(len(data)), data, width=0.6,
        # bottom=[0, 0, 0, 0]    # 设置底部从何值开始
        # facecolor='#6495ED',  # 颜色
        # edgecolor='red',
        # linestyle='--',
        # linewidth=1,   # 柱状图边框
        tick_label=labels  # tick_label
        )
plt.show()


# 堆叠柱状图
x = ['A', 'B', 'C', 'D', 'E']
a = [2, 3, 4, 5, 6]
b = [2, 3, 4, 5, 6]

plt.bar(x, a, label='a')
plt.bar(x, b, bottom=a, label='b')
plt.legend()
plt.show()


# 并列柱状图
x = np.arange(5)
a = [2, 3, 4, 5, 6]
b = [1, 2, 2, 1, 1]
c = [2, 3, 2, 3, 2]
labels = ['A', 'B', 'C', 'D', 'E']
total_width, n = 0.8, 3
width = total_width/n

labels = ['A', 'B', 'C', 'D', 'E']
plt.bar(x, a, width=width, label='a')
plt.bar(x + width, b, width=width, label='b', tick_label=labels)
plt.bar(x + 2*width, c, width=width, label='c')
plt.legend()
plt.show()


# 正负条形图
a = np.array([5, 20, 15, 25, 10])
b = np.array([10, 15, 20, 15, 5])

plt.barh(range(len(a)), a)
plt.barh(range(len(b)), -b)
plt.show()
