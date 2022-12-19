from pyecharts.globals import CurrentConfig, NotebookType

CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
from pyecharts.charts import Geo, Map, BMap
from pyecharts import options as opts
import json
import pandas as pd

with open('shoesV2.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)
data = pd.json_normalize(data)
data.sales = data.sales.apply(lambda x: x.split('人付款')[0]).astype(int)
data.dropna(subset=['info.款式'], inplace=True)
data['province'], data['city'] = data.location.str.split(' ', 1).str
province = data[['nick', 'sales', 'province']].groupby(by=['province'], sort=False).sum().sort_values(by=['sales'],
                                                                                                      ascending=False)[
           0:6]
zhejiang = data[data.province == '浙江']
city = zhejiang[['nick', 'sales', 'city']].groupby(by=['city'], sort=False).sum().sort_values(by=['sales'],
                                                                                              ascending=False)[0:6]
print(province)
print(city)
provinceList = [z for z in province.sales.items()]
cityList = [z for z in city.sales.items()]
geo = Geo()
geo.add_schema(maptype='浙江')
geo.add('浙江商品销量分布-Geo', cityList, label_opts=opts.LabelOpts(is_show=True), type_=GeoType.EFFECT_SCATTER,
        symbol_size=15)
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(is_piecewise=True, max_=19000),
                    title_opts=opts.TitleOpts(title="浙江商品销量销售情况"))
geo.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
geo.render_notebook()
geo = Geo()
geo.add_schema(maptype='china')
geo.add('浙江商品销量分布-Geo', provinceList, label_opts=opts.LabelOpts(is_show=True), type_=GeoType.EFFECT_SCATTER,
        symbol_size=15)
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(is_piecewise=True, max_=23000),
                    title_opts=opts.TitleOpts(title="浙江商品销量销售情况"))
geo.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
geo.render_notebook()
eachCity = []
for i in city.sales.items():
    eachCity.append([i[0] + "市", i[1]])
map = Map()
map.add("浙江省商品销量-Map", eachCity, "浙江")
map.set_global_opts(
    title_opts=opts.TitleOpts(title="浙江省商品销量分布情况"),
    visualmap_opts=opts.VisualMapOpts(max_=19000, is_piecewise=True),
)
map.render_notebook()
map = Map()
map.add("Map-visualMap全国商品分布图", provinceList, "china")
map.set_global_opts(
    title_opts=opts.TitleOpts(title="浙江省商品销量分布情况"),
    visualmap_opts=opts.VisualMapOpts(max_=19000, is_piecewise=True),
)
map.render_notebook()

BAIDU_AK = "K2n5m9GXasQFV5arkjpCGsXL"
bmap = BMap()
bmap.add_schema(
    baidu_ak=BAIDU_AK,
    center=[120.21201, 30.2084], zoom=7
)
bmap.add("全国商品销量分布图-Bmap", cityList, label_opts=opts.LabelOpts(formatter="{b}"))
bmap.set_global_opts(title_opts=opts.TitleOpts(title="BMap-全国商品销量分布图"),
                     visualmap_opts=opts.VisualMapOpts(max_=23000, is_piecewise=True))
bmap.render_notebook()
BAIDU_AK = "K2n5m9GXasQFV5arkjpCGsXL"
bmap = BMap()
bmap.add_schema(
    baidu_ak=BAIDU_AK,
    center=[120.13066322374, 30.240018034923],
)
bmap.add("全国商品销量分布图-Bmap", provinceList, label_opts=opts.LabelOpts(formatter="{b}"))
bmap.set_global_opts(title_opts=opts.TitleOpts(title="BMap-全国商品销量分布图"),
                     visualmap_opts=opts.VisualMapOpts(max_=23000, is_piecewise=True))
bmap.render_notebook()
