import matplotlib.pyplot as plt
import numpy as np

from random_walk import RandomWalk
from settings import (set_plot_style,
                      set_axes_style,
                      save_fig,
                      set_layout_style)

# ==================== 全局参数设置 ====================
set_plot_style()

# ==================== 创建图形和坐标轴 ====================
# 使用subplots()创建图形和坐标轴对象
fig, ax = plt.subplots()
# 开启交互模式
plt.ion()
# ==================== 创建数据 ====================
# 创建一个 RandomWalk 实例
rw = RandomWalk()
# rw.fill_walk()
# 初始化空散点图
# scatter = ax.scatter([], [], marker='o', s=15, alpha=0.7, color='#1f77b4')
set_axes_style(ax)
set_layout_style()
# 第一次显示
# plt.show()

while len(rw.x_values) < rw.num_points:
    rw.fill_walk_one_step()
    # print(len(rw.x_values))
    x = rw.x_values[-1]
    y = rw.y_values[-1]
    ax.scatter(x, y, marker='o', s=15,
               facecolor='none', edgecolor='red', linewidth=2, alpha=len(rw.x_values) / rw.num_points)
    # point_numbers = range(len(rw.x_values))
    plt.draw()  # 显示图形
    plt.pause(0.0001)  # 暂停0.5秒
    set_axes_style(ax)
    set_layout_style()

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
