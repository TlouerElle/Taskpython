# 导入模块
import matplotlib.pyplot as plt
from faker import Faker
import palettable
import pandas as pd
import numpy as np
import random

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置画图中文
random.seed(10)  # 设置随机种子
fake = Faker(locale='zh_CN')  # 伪随机数据设置中文
fake.random.seed(0)  # 伪随机随机种子设置
# 生成8个中文的姓名的伪随机数据列表
names = []
for i in range(0, 8):
    names.append(fake.name())
print(names)
fig, axes = plt.subplots(2, 2, figsize=(20, 20))  # 子图
# 生成成绩范围要求在60-100分区间的随机整数score1、score2、score3的dataframe
df = pd.DataFrame(np.random.randint(60, 100, size=(8, 3)), index=names, columns=['score1', 'score2', 'score3'])
print(df)
# kind作图类型分别为多系列柱状图多系列柱状图、折线图、面积图、饼图；ax子图位置；grid是否显示网格；color配合palettable调色盘使用；style条形图样式；autopct百分比类型
df.plot(kind='bar', ax=axes[0, 0], grid=False, color=palettable.colorbrewer.qualitative.Dark2_7.mpl_colors)
df.plot(kind='line', style='--o', ax=axes[0, 1], grid=False,
        color=palettable.colorbrewer.qualitative.Dark2_7.mpl_colors)
df.plot(kind='area', ax=axes[1, 0], grid=False, color=palettable.colorbrewer.qualitative.Dark2_7.mpl_colors)
df.plot(kind='pie', y='score1', autopct='%1.1f%%', ax=axes[1, 1], grid=False,
        colors=palettable.cartocolors.qualitative.Bold_9.mpl_colors)
plt.show()
