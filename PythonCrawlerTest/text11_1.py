import pymysql
import requests
from lxml import etree



def download_html(url):
    response = requests.get(url, timeout=5)
    if response.status_code != 200:
        return
    html = etree.HTML(response.text)
    title = html.xpath("//li/div[@class='book-info']/h3/a/text()")
    author = html.xpath("//ul/li/div[@class='book-info']/h4/a[@class='default']/text()")
    category = html.xpath("//li/div[@class='book-info']/p[@class='tag']/span[@class='org']/text()")
    state = html.xpath("//ul/li/div[@class='book-info']/p[@class='tag']/span[@class='pink']/text()")
    count = html.xpath("//ul/li/div[@class='book-info']/p[@class='tag']/span[@class='blue']/text()")
    content = html.xpath("//ul/li/div[@class='book-info']/p[@class='intro']/text()")
    for i in range(0, 20):
        sql = "INSERT hongxiu_xdyq(title, author, category, state, count,content) VALUES(%s,%s,%s,%s,%s,%s)"
        connect(sql, (title[i], author[i], category[i], state[i], count[i], content[i]))
        print(title[i], author[i], category[i], state[i], count[i])


def connect(sql, data):
    conn = pymysql.connect(host='localhost', user='root', password='root', database='cralwer', port=3306)
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    urls = ['https://www.hongxiu.com/category/30020_f1_f1_f1_f1_f1_0_{}'.format(i) for i in range(1, 51)]
    for url in urls:
        print(url,end='')
        download_html(url)
