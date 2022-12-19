import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
print(df)

# titanic中不同船舱类别妇女儿童男性的总人数
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title("Total number")  # 设置标题
# x分类为船舱class data为数据 hue按照who分类 order排序 palette颜色
sns.countplot(x='class', data=df, hue='who', order=['Third', 'Second', 'First'], palette='husl')
# 在直方图上显示具体数值
for p in ax.patches:
    ax.annotate(f'\n{p.get_height()}', (p.get_x(), p.get_height()), color='black', size=12)
ax.set_ylabel('total')  # 设置y标签
plt.show()
# titanic不同船舱类别妇女儿童男性的生存人数
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title("survived")
survived = df[df.survived == 1]  # 生存者的dataFrame
sns.countplot(x='class', data=survived, hue='who', order=['First', 'Second', 'Third'], palette='husl')
for p in ax.patches:
    ax.annotate(f'\n{p.get_height()}', (p.get_x(), p.get_height()), color='black', size=12)
ax.set_ylabel('total')
plt.show()
# titanic不同船舱类别妇女儿童男性的生产率
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title("survived")
# ci=None不描绘错误条
sns.barplot(x='class', y='survived', hue='who', data=df, order=['First', 'Second', 'Third'], palette='husl', ci=None)
for p in ax.patches:
    ax.annotate(f"\n{'%.2f' % p.get_height()}", (p.get_x(), p.get_height()), color='black', size=12)
ax.set_ylabel('survived')
plt.show()
