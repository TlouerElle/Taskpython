import matplotlib.pyplot as plt
import csv
from wordcloud import WordCloud

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 显示中文标签,处理中文乱码问题
plt.rcParams['axes.unicode_minus'] = False  # 坐标轴负号的处理
author_dict = {}
f = open(r'author.txt', 'r', encoding='utf-8')
for author in f.readlines():
    if author not in author_dict:
        author_dict[author] = 1
    else:
        author_dict[author] += 1
author_value_list = []
author_key_list = []
for key in author_dict:
    author_value_list.append(author_dict[key])
    author_key_list.append(key)


def author_cake():
    plt.axes(aspect='equal')  # 将横、纵坐标轴标准化处理，确保饼图是一个正圆，否则为椭圆
    explode = [0, 0, 0, 0, 0, 0]
    plt.pie(x=author_value_list,  # 绘图数据
            explode=explode,  # 指定饼图某些部分的突出显示，即呈现爆炸式
            labels=author_key_list,  # 添加教育水平标签
            autopct='%.2f%%',  # 设置百分比的格式，这里保留两位小数
            pctdistance=0.5,  # 设置百分比标签与圆心的距离
            labeldistance=1.1,  # 设置教育水平标签与圆心的距离
            startangle=180,  # 设置饼图的初始角度
            radius=1.2,  # 设置饼图的半径
            counterclock=False,  # 是否逆时针，这里设置为顺时针方向
            wedgeprops={'linewidth': 1.5, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
            textprops={'fontsize': 15, 'color': 'black'},  # 设置文本标签的属性值
            )
    plt.title('作者作品分布')
    plt.show()


def author_column():
    plt.bar(range(len(author_key_list)), author_value_list, tick_label=author_key_list)
    plt.xlabel('作者')
    plt.ylabel('发表数')
    for i in range(len(author_value_list)):
        plt.text(x=i - 0.05, y=author_value_list[i] + 0.2, s='%d' % author_value_list[i])
    plt.show()


def star():
    star_list = []
    file = r'funny-data-csv.csv'
    with open(file, encoding='utf-8') as jd:
        for i in range(1):
            jd.readline()
        for row in csv.reader(jd):
            star_list.append(row[2])
    x = range(len(star_list))  # x轴数据
    y = star_list  # y轴数据
    plt.plot(x, y, 'o')  # 第一个参数是x轴的数据  第二个参数是y轴的数据  第三个参数是展现形式
    plt.show()


def classification():
    classification_dict = {}
    f = open(r'classification.txt', 'r', encoding='utf-8')
    for classification in f.readlines():
        classification2 = classification.split(' ')
        for classification in classification2:
            if classification not in classification_dict and len(classification) > 1:
                classification_dict[classification] = 1
            elif len(classification) > 1:
                classification_dict[classification] += 1
    classification_value_list = []
    classification_key_list = []
    for key in classification_dict:
        classification_value_list.append(classification_dict[key])
        classification_key_list.append(key)
    x = range(len(classification_key_list))  # x轴数据
    y = classification_value_list  # y轴数据
    plt.scatter(x, y, s=50, edgecolor='none')
    plt.title("总数", fontsize=15)
    plt.xlabel("类别", fontsize=15)
    plt.ylabel("y", fontsize=15)
    plt.tick_params(axis='both', labelsize=15)
    plt.plot(x, y, linewidth=5)
    plt.show()


def english_word_cloud():
    path = r"title.txt"

    with open(path, 'r', encoding="utf-8") as f:
        cut_text = f.read()
        print(cut_text)
        pass
    word_cloud = WordCloud(
        background_color="white",
        width=1920,
        height=1080
    ).generate(cut_text)
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    author_cake()
    author_column()
    star()
    classification()
    english_word_cloud()
