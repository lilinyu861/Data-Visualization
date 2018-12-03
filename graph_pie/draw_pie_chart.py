# draw pie chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 有比例详情的饼图
labels = [u'a', u'b', u'c', u'd']
sizes = [1, 2, 3, 4]
colors = ['#DC443C', '#FFD700', '#6495ED', '#32CD46']  # 红黄蓝绿
explode = (0, 0, 0, 0)  # 如果想让某部分爆出来可以修改值为0.6
plt.pie(sizes, explode, labels, colors, autopct='%3.2f%%', shadow=False, startangle=50, pctdistance=0.6)
# pctdistance 是数值距离圆心半径倍数距离
# startangle 逆时针起始角度设置
plt.axis('equal')
plt.legend()  # 增加
plt.show()
