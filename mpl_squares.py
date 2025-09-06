import matplotlib.pyplot as plt
import numpy as np
import scienceplots

# 设置全局参数
# plt.rcParams['figure.figsize'] = [10, 6]  # 图像尺寸（宽，高）
# plt.rcParams['figure.dpi'] = 100  # 分辨率
# plt.rcParams['savefig.dpi'] = 300  # 保存图像的分辨率
# plt.rcParams['font.size'] = 12  # 字体大小
# plt.rcParams['lines.linewidth'] = 2  # 线条宽度
# 禁用 LaTeX 渲染
plt.rcParams['text.usetex'] = False
# 查看可用样式
print(plt.style.available)
# plt.style.use(['science', 'ieee', 'grid'])  # 需要安装 scienceplots 包
# plt.style.use('science')
# plt.style.use('_mpl-gallery')
# plt.style.use('seaborn-v0_8-whitegrid')
# 或者自定义样式
# plt.style.use({
#     'figure.figsize': (10, 6),
#     'font.size': 12,
#     'axes.titlesize': 16,
#     'axes.labelsize': 14,
#     'xtick.labelsize': 12,
#     'ytick.labelsize': 12,
#     'legend.fontsize': 11
# })

# 创建高质量图像
fig, ax = plt.subplots()
# fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

# 生成数据
# x = range(1, 6, 1)
# print(x)
# squares = [1, 4, 9, 16, 25]
# x=np.arange(1, 10, 1)
x=np.linspace(1, 10, 100)
# y=np.power(x, 2)
y=np.sin(x)
# print(type(squares))


# 绘制图形
ax.plot(x, y)
# ax.plot(x, y + 2.5, 'x', markeredgewidth=2)
# ax.plot(x, y, linewidth=2.0)
# ax.plot(x, y - 2.5, 'o-', linewidth=2)
# ax.plot(x, y, linewidth=2.5, color='blue', label='正弦曲线')
# ax.set_xlabel('X轴', fontsize=14)
# ax.set_ylabel('Y轴', fontsize=14)
# ax.set_title('高质量正弦曲线图', fontsize=16)
# ax.legend(fontsize=12)
# ax.grid(True, alpha=0.3)
# ax.set(xlim=(0, 20), xticks=np.arange(1, 20),
#        ylim=(0, 40), yticks=np.arange(1, 40))

# 调整布局
# plt.tight_layout()



# 显示图像
plt.show()

# 保存高质量图像
# fig.savefig('high_quality_plot.png', dpi=300, bbox_inches='tight',
           # facecolor='white', edgecolor='none')

