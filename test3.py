import matplotlib.pyplot as plt
import numpy as np
import random
import time
from math import *

plt.ion()  # 开启interactive mode 成功的关键函数
plt.figure(1)
t = np.linspace(0, 20, 100)


for i in range(100):
    # plt.clf() # 清空画布上的所有内容。此处不能调用此函数，不然之前画出的轨迹，将会被清空。
    y = np.sin(t * i / 100)
    # plt.plot(t, y)  # 一条轨迹
    # plt.figure(1)
    # plt.scatter(t, y)
    random_color = (random.random(), random.random(), random.random())
    plt.plot(t, y,color=random_color,linewidth=1)
    # plt.draw(block=False)
    plt.draw()  # 注意此函数需要调用
    # time.sleep(1)
    plt.pause(0.1)

plt.ioff()
plt.show()

# plt.show()
