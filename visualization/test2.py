# 导入包
import pandas as pd
import matplotlib.pyplot as plt

plt.title('shopData')  # 标题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体避免乱码

shopData = pd.DataFrame(pd.read_csv(r'D:\pythonProject\visualization\shopsData.csv', nrows=10))  # 读取文件
name = list(shopData['name'])  # 提取name作为横坐标
quality = list(shopData['quality'])
environment = list(shopData['environment'])
service = list(shopData['service'])
plt.xticks(rotation=90)  # 字体旋转90度
plt.plot(name, quality, marker='o')  # 质量折线图
plt.plot(name, environment, marker='*')  # 环境折线图
plt.plot(name, service, marker='d')  # 服务折线图
plt.legend(['quality', 'environment', 'service'])   # 标签
plt.show()
