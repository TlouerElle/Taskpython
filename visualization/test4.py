import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file = pd.read_csv('seeds.data', sep=',', header=None)  # 省略头部读取data文件
dataArr = np.array(file)  # 转换成数组
data = pd.DataFrame(dataArr, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'ttype'])  # 转换成dataFrame并添加列
print(data)
# pairplot显示特征两两关系 vars选取特征 diag_kind控制对角线上图的类型  kind控制非对角线上图的类型 hue对某字段进行分类
sns.pairplot(data, vars=['a', 'b', 'c', 'd', 'e', 'f', 'g'], diag_kind='kde', hue='ttype')
sns.pairplot(data, vars=['a', 'b', 'c'], diag_kind='kde', hue='ttype', kind='reg')
# map_diag(plt.hist)对角线单变量子图 map_offdiag(sns.kdeplot)非对角线
sns.PairGrid(data, vars=['a', 'd', 'e'], hue="ttype").map_diag(plt.hist).map_offdiag(sns.kdeplot)
