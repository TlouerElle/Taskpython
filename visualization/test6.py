from pyecharts.charts import Bar, Line, Tab
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import json
import pandas as pd

#   数据预处理
with open('shoesV2.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)
data = pd.json_normalize(data)  # json转换为dataFrame
data.sales = data.sales.apply(lambda x: x.split('人付款')[0]).astype(int)  # 销量处理为int
data.dropna(subset=['info.款式'], inplace=True)  # Nan的处理
top4Shop = data[['nick', 'sales']].groupby(by=['nick'], sort=False).sum().sort_values(by=['sales'],
                                                                                      ascending=False).index[
           0:4].tolist()  # 排序提取销量前4的商店
shop0 = data[data.nick == top4Shop[0]][['sales', 'info.款式']].groupby(by=['info.款式']).sum()  # 销量第1
shop1 = data[data.nick == top4Shop[1]][['sales', 'info.款式']].groupby(by=['info.款式']).sum()  # 销量第2
shop2 = data[data.nick == top4Shop[2]][['sales', 'info.款式']].groupby(by=['info.款式']).sum()  # 销量第3
shop3 = data[data.nick == top4Shop[3]][['sales', 'info.款式']].groupby(by=['info.款式']).sum()  # 销量第4
# 重新组成新的dataFrame重新处理Nan
top4 = pd.merge(shop0, shop1, on='info.款式', how='outer')
top4 = pd.merge(top4, shop2, on='info.款式', how='outer')
top4 = pd.merge(top4, shop3, on='info.款式', how='outer')
top4.columns = top4Shop
top4 = top4.fillna(0)
print(top4)
# 绘制饼图
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 主题设置
bar.add_xaxis(top4.index.tolist())
bar.add_yaxis('{}'.format(top4Shop[0]), top4.意尔康皮鞋旗舰店.tolist())
bar.add_yaxis('{}'.format(top4Shop[1]), top4.意尔康男鞋旗舰店.tolist())
bar.add_yaxis('{}'.format(top4Shop[2]), top4.乙方乙方88888.tolist())
bar.add_yaxis('{}'.format(top4Shop[3]), top4.意尔康品牌店.tolist())
# 字体旋转、标题、工具栏
bar.set_global_opts(xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 45}),
                    title_opts=opts.TitleOpts(title="排名前4商铺销售情况"), toolbox_opts=opts.ToolboxOpts(is_show=True))

line = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
line.add_xaxis(top4.index.tolist())
line.add_yaxis('{}'.format(top4Shop[0]), top4.意尔康皮鞋旗舰店.tolist())
line.add_yaxis('{}'.format(top4Shop[1]), top4.意尔康男鞋旗舰店.tolist())
line.add_yaxis('{}'.format(top4Shop[2]), top4.乙方乙方88888.tolist())
line.add_yaxis('{}'.format(top4Shop[3]), top4.意尔康品牌店.tolist())
line.set_global_opts(xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 45}),
                     title_opts=opts.TitleOpts(title="排名前4商铺销售情况"),
                     toolbox_opts=opts.ToolboxOpts(is_show=True))
# 选项卡
tab = Tab()
tab.add(bar, '排名前4店商铺售情况柱状图选项卡')
tab.add(line, '排名前4店商铺售情况折线图选项卡')
tab.render_notebook()
