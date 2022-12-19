import requests
from lxml import etree
import pymysql


def download(url):
    try:
        response = requests.get(url)
        if response.status_code != 200: return
        data = response.text
        html = etree.HTML(data)
        imgurl = html.xpath('//*[@id="imageContent"]/section/div/figure/a/img/@data-src')
        count = 1
        for url in imgurl:
            url = 'https:' + url
            imgname = url.split('/')[-1]
            print('{} pictures completed for the current website'.format(count))
            response = requests.get(url)
            imgbytes = response.content
            count += 1
            sql = "INSERT vcg_bigdata(img_name, img_bytes, img_url) VALUES(%s, %s, %s)"
            connect(sql, (imgname, imgbytes, url))
    except Exception as er:
        print(er)


def connect(sql, data):
    conn = pymysql.connect(host='159.75.52.80', user='root', password='bigdata2019', database='db_WeiEnsong', port=3306)
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    urls = ['https://www.vcg.com/creative-image/dashuju/?page={}'.format(i) for i in range(1, 100)]
    for url in urls:
        print(url)
        download(url)
