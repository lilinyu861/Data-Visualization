import numpy as np
import matplotlib.pyplot as plt


# 简单的散点图
plt.title("this is a simple diagram")
plt.xlim(xmax=7, xmin=0)
plt.ylim(ymax=7, ymin=0)
plt.xlabel("x")
plt.ylabel("y")
plt.plot([1, 2, 3], [4, 5, 6], 'ro')
plt.show()
