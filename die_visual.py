from die import Die
import plotly.express as px

# '''一个骰子！！！！！！！！！！！！！！！'''
# # 创建一个 D6
# die = Die()
# # 掷几次骰子并将结果存储在一个列表中
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
# # print(results)
#
# # 分析结果
# frequencies = []
# poss_results = range(1, die.num_sides + 1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)
# # print(frequencies)
# # 对结果进行可视化
# # fig = px.bar(x=poss_results, y=frequencies)
# title = "Results of Rolling One D6 1,000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title,
#              labels=labels)
# fig.show()


'''两个骰子！！！！！！！！！！！！！！！'''
# 创建一个 D6
die_1 = Die()
die_2 = Die(10)
# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# print(results)

# 分析结果
frequencies = []
poss_results = range(1, die_1.num_sides+die_2.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)
# 对结果进行可视化
# fig = px.bar(x=poss_results, y=frequencies)
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title,
             labels=labels)
# 进一步定制图形
fig.update_layout(xaxis_dtick=1)
fig.show()
fig.write_html('dice_visual_d6d10.html')
