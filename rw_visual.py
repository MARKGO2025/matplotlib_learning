import matplotlib.pyplot as plt
from random_walk import RandomWalk

# ==================== 创建数据 ====================
# 创建一个 RandomWalk 实例
rw = RandomWalk()
rw.fill_walk()
x = rw.x_values
y = rw.y_values
point_numbers=range(rw.num_points)

# ==================== 创建图形和坐标轴 ====================
# 使用subplots()创建图形和坐标轴对象
fig, ax = plt.subplots()

# ==================== 绘制折线图 ====================

# ax.plot(x, y1, label='Sine Wave', marker='o', markevery=10, color='#1f77b4')
# ax.scatter(x, y1, label='Sine Wave', marker='o', color='#1f77b4', s=10)
ax.scatter(x, y, label='rank walk', marker='o',
           s=15, c=point_numbers, cmap=plt.get_cmap('Blues'))
ax.scatter(x[-1], y[-1], label='Final Position', marker='o', color='Red', s=10)



# ==================== 设置坐标轴标签和标题 ====================
ax.set_xlabel('X', fontweight='bold')  # x轴标签，加粗
ax.set_ylabel('Y', fontweight='bold')  # y轴标签，加粗
ax.set_title('Rank Walk Map', fontweight='bold')  # 标题，加粗
# ==================== 设置图例 ====================
# 添加图例，位置在右上角，显示边框，边框颜色为黑色
ax.legend(loc='upper right', frameon=True, edgecolor='black')

# ==================== 设置网格 ====================
ax.grid(True, alpha=0.5)  # 显示网格，透明度50%

# ==================== 设置坐标轴范围 ====================
# ax.set_xlim(0, 10)  # x轴范围：0到10
# ax.set_ylim(-1.2, 1.2)  # y轴范围：-1.2到1.2
ax.set_aspect('equal')
# 隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# ==================== 设置刻度 ====================
# 设置主刻度的线宽
ax.tick_params(axis='both', which='major', width=0.8)

# ==================== 保存图像 ====================
# 保存为PDF格式（矢量图，论文推荐格式）
plt.savefig('academic_line_plot.pdf')
# 同时保存为PNG格式（位图，便于预览）
plt.savefig('academic_line_plot.png', dpi=300)

# ==================== 显示图形 ====================
plt.tight_layout()  # 自动调整布局，避免元素重叠
plt.show()  # 显示图形
# print("论文风格折线图生成完成！已保存为PDF和PNG格式。")




def set_plot_style():
    # ==================== 全局参数设置 ====================
    # 字体设置
    plt.rcParams['font.family'] = 'serif'  # 使用衬线字体（学术论文常用）
    plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']  # 优先使用Times New Roman
    plt.rcParams['font.size'] = 12  # 基础字体大小
    # 坐标轴设置
    plt.rcParams['axes.labelsize'] = 12  # 坐标轴标签字体大小
    plt.rcParams['axes.titlesize'] = 14  # 标题字体大小
    plt.rcParams['axes.linewidth'] = 0.8  # 坐标轴线宽
    # 线条和标记设置
    plt.rcParams['lines.linewidth'] = 2  # 线宽（确保线条清晰可见）
    plt.rcParams['lines.markersize'] = 6  # 标记点大小
    # 刻度设置
    plt.rcParams['xtick.labelsize'] = 10  # x轴刻度标签大小
    plt.rcParams['ytick.labelsize'] = 10  # y轴刻度标签大小
    # 图例设置
    plt.rcParams['legend.fontsize'] = 10  # 图例字体大小
    plt.rcParams['legend.frameon'] = True  # 显示图例边框
    plt.rcParams['legend.framealpha'] = 1.0  # 图例背景不透明
    plt.rcParams['legend.fancybox'] = False  # 不使用圆角边框（学术风格更正式）
    # 网格设置
    plt.rcParams['grid.linestyle'] = '--'  # 网格线样式（虚线）
    plt.rcParams['grid.alpha'] = 0.7  # 网格线透明度
    # 图像输出设置
    plt.rcParams['figure.dpi'] = 300  # 显示分辨率（确保清晰度）
    plt.rcParams['savefig.dpi'] = 300  # 保存分辨率（高质量输出）
    plt.rcParams['savefig.bbox'] = 'tight'  # 紧凑边框（避免多余空白）
    plt.rcParams['savefig.format'] = 'pdf'  # 保存格式（矢量图，推荐用于论文）
    # 图像尺寸设置
    plt.rcParams['figure.figsize'] = [10, 6]  # 图像尺寸（宽度10英寸，高度6英寸）

