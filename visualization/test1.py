# 导入模块

import pandas as pd
import csv

# 按行读取商铺数据文件，并除去空格、\t等其他不需要的字符并重新写入一个新的csv,comment，price中的中文移除。

with open('商铺数据.csv', "r+",encoding='utf-8') as file:
    for line in file:
        record = line.replace(' ', '').replace('\n', '').replace('\ufeff', ' ').replace('我要点评', '0').replace('条点评', '0').replace('人均￥', '').replace('人均-', '0').replace('环境', ' ').replace('服务', ' ').replace('效果', '').replace('质量', '').replace('口味', '').replace('总分', '').replace('产品', '').split(',')
        with open ('shopData.csv','a+', encoding='utf-8-sig', newline='') as fp:
            writer = csv.writer(fp)
            writer.writerows([record])
# 重新读取新生成的csv转化为dataFrame并且含有空的行删除，即清除字段缺失的数据


shopsData = pd.read_csv('shopData.csv').dropna(axis=0)
# 分割commentlist中的三个数据

shopsData['quality'] = shopsData['commentlist'].map(lambda x: x.split(' ')[0])
shopsData['environment'] = shopsData['commentlist'].map(lambda x: x.split(' ')[1])
shopsData['service'] = shopsData['commentlist'].map(lambda x: x.split(' ')[2])
shopsData.to_csv('shopsData.csv', encoding='utf-8-sig', index=False)
dict1 = shopsData.to_dict('records')
print(dict1)