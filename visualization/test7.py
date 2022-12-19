from pyecharts.charts import Pie, Funnel, Timeline
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import json
import pandas as pd

with open('shoesV2.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)
data = pd.json_normalize(data)
data.sales = data.sales.apply(lambda x: x.split('人付款')[0]).astype(int)
data.dropna(subset=['info.款式'], inplace=True)
top4Shop = data[['nick', 'sales']].groupby(by=['nick'], sort=False).sum().sort_values(by=['sales'],
                                                                                      ascending=False).index[
           0:4].tolist()
shop0 = data[data.nick == top4Shop[0]][['sales', 'info.款式']].groupby(by=['info.款式']).sum()
shop1 = data[data.nick == top4Shop[1]][['sales', 'info.款式']].groupby(by=['info.款式']).sum()
shop2 = data[data.nick == top4Shop[2]][['sales', 'info.款式']].groupby(by=['info.款式']).sum()
shop3 = data[data.nick == top4Shop[3]][['sales', 'info.款式']].groupby(by=['info.款式']).sum()
top4 = pd.merge(shop0, shop1, on='info.款式', how='outer')
top4 = pd.merge(top4, shop2, on='info.款式', how='outer')
top4 = pd.merge(top4, shop3, on='info.款式', how='outer')
top4.columns = top4Shop
top4 = top4.fillna(0)
print(top4)
# 绘制饼图
pie = Pie()
pie.add('', [list(z) for z in zip(top4Shop, top4[2:3].values.tolist()[0])])
# 标题、标签在右纵向显示
pie.set_global_opts(title_opts=opts.TitleOpts(title='排名前4男鞋里休闲皮鞋的销售情况'),
                    legend_opts=opts.LegendOpts(type_="scroll", pos_left="right", orient="vertical"))
# 绘制漏斗图
funnel = Funnel()
funnel.add('', [list(z) for z in zip(top4Shop, top4[2:3].values.tolist()[0])])
funnel.set_global_opts(title_opts=opts.TitleOpts(title='排名前4男鞋里休闲皮鞋的销售情况'))

# 时间线
timeline = Timeline(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
timeline.add(pie, '排名前4休闲皮鞋销售饼图')
timeline.add(funnel, '排名前4休闲皮鞋销漏斗图')
timeline.render_notebook()
