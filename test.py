import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y1 = np.sin(x)  # 正弦波
y2 = np.cos(x)  # 余弦波
y3 = 0.5 * np.sin(x) + 0.5  # 缩放和平移后的正弦波

plt.ion()
# fig, ax = plt.subplots()
plt.figure(1)
plt.scatter(x, y1, marker='o', s=10, color='#ff7f0e')
plt.tight_layout()  # 自动调整布局，避免元素重叠
# plt.draw()
# plt.show(block=False)
# plt.show()  # 显示图形
plt.pause(1)  # 让图形有时间渲染
plt.scatter(x, y2, marker='o', s=10, color='#2ca02c')
# plt.draw()
# plt.show(block=False)
plt.pause(1)  # 让图形有时间渲染
plt.ioff()
plt.show()



# x = np.linspace(0, 10, 100)
# x=range(1,10,2)
# x=[value**2 for value in range(1, 11)]
# print(type(x))
# # x=list(range(1,10,2))
# # print(type(x))
# for i in x:
#     print(i)

# print(len(x),type(x))
