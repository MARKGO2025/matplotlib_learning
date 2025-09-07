import matplotlib.pyplot as plt
import numpy as np
import random
import time
from math import *
from settings import (set_plot_style,
                      set_axes_style,
                      save_fig,
                      set_layout_style)

# ==================== 全局参数设置 ====================
set_plot_style()
# 开启交互模式
plt.ion()
# ==================== 创建图形和坐标轴 ====================
fig, ax = plt.subplots()
# ==================== 创建数据 ====================
plt.plot([], [])
plt.draw()  # 注意此函数需要调用
set_axes_style(ax)
set_layout_style()
# ==================== 创建图形和坐标轴 ====================
fig2, ax2 = plt.subplots()
# ==================== 创建数据 ====================
plt.plot([], [])
plt.draw()  # 注意此函数需要调用
set_axes_style(ax2)
set_layout_style()
t = np.linspace(0, 20, 100)
for i in range(100):
    # plt.clf() # 清空画布上的所有内容。此处不能调用此函数，不然之前画出的轨迹，将会被清空。
    y = np.sin(t * i / 100)
    # plt.plot(t, y)  # 一条轨迹
    plt.figure(np.mod(i,2)+1)
    # plt.scatter(t, y)
    random_color = (random.random(), random.random(), random.random())
    plt.plot(t, y,color=random_color,linewidth=1)
    plt.draw()  # 注意此函数需要调用
    # time.sleep(1)
    plt.pause(0.1)
plt.ioff()
plt.show()
# ==================== 绘制折线图 ====================
# ax.plot(x, y1, label='Sine Wave', marker='o', markevery=10, color='#1f77b4')
# ax.scatter(x, y1, label='Sine Wave', marker='o', color='#1f77b4', s=10)
# ax.scatter(x, y, label='rank walk', marker='o',
#            s=15, c=point_numbers, cmap=plt.get_cmap('Blues'))
# ax.scatter(x, y, label='rank walk', marker='o',
#            s=15, c=point_numbers, cmap=plt.get_cmap('Blues'))
# ax.scatter(x[-1], y[-1], label='Final Position', marker='o', color='Red', s=10)

# set_axes_style(ax)
# ==================== 保存图像 ====================
# img_name = 'academic_line_plot'
# save_fig(img_name)
# ==================== 显示图形 ====================
# set_layout_style()

# print("论文风格折线图生成完成！已保存为PDF和PNG格式。")
