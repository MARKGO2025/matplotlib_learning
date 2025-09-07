import matplotlib.pyplot as plt
import numpy as np
import time
from math import *

# plt.ion()  # 开启interactive mode 成功的关键函数
# plt.figure(1)
# t = [0]
# t_now = 0
# m = [t_now]
#
# for i in range(1000):
#     plt.clf()  # 清空画布上的所有内容
#     t_now = i
#     t.append(t_now)  # 模拟数据增量流入，保存历史数据
#     m.append(t_now)  # 模拟数据增量流入，保存历史数据
#     plt.scatter(t, m,  marker='o', s=10, color='#2ca02c')
#     # plt.draw()#注意此函数需要调用
#     # time.sleep(0.01)
#     plt.pause(0.01)


# plt.figure(1)
# plt.subplot(2,1,1)
# plt.plot([1,2,3])
# plt.subplot(2,1,2)
# plt.plot([4,5,6])
# plt.show()
#
# plt.figure(2)
# plt.plot([4,5,6])
# plt.show()
#
# plt.figure(1)
# plt.subplot(2,1,2)
# plt.title("第1张画图的第2个子图",fontproperties="SimHei")
# plt.show()