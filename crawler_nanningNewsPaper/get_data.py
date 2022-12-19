import requests
from lxml import etree
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43',

}
g_url = []


def get_url(url):
    global g_url
    res = requests.get(url, headers=headers, timeout=20, stream=True, verify=False)
    if res.status_code != 200:
        return
    html = etree.HTML(res.text)
    page = len(html.xpath("//a[@class='bmdh_con_a']/text()"))
    if page < 10:
        url = [url.replace('.htm', '') + '_content_00{}.htm'.format(i) for i in range(0, page)]
        for i in url:
            g_url.append(i)
    if page > 9:
        url1 = [url.replace('.htm', '') + '_content_00{}.htm'.format(i) for i in range(0, 10)]
        url2 = [url.replace('.htm', '') + '_content_0{}.htm'.format(i) for i in range(10, page)]
        url = url1 + url2
        for i in url:
            g_url.append(i)
    return g_url


def get_data(url):
    try:
        res = requests.get(url, headers=headers, timeout=20, stream=True, verify=False)
        if res.status_code != 200:
            return
        res.encoding = 'utf-8'
        html = etree.HTML(res.text)
        subtitle = ''
        content = ''
        title = html.xpath("//div[@class='bmnr_con_biaoti']/text()")[0]
        subtitle_list = html.xpath("//div[@class='bmnr_con_yinti'][2]/text()")
        if len(subtitle_list) == 0:
            subtitle = ' '
        else:
            for i in subtitle_list:
                subtitle = subtitle + i
        content_list = html.xpath("//div[@id='zoom']/text()")
        if len(content_list) == 0:
            content = ' '
        else:
            for i in content_list:
                content = content + i
        with open(r'NanNing_data.csv', 'a+', encoding='utf-8') as f:
            row = [title, subtitle, content]
            writer = csv.writer(f)
            writer.writerow(row)
            print(title, subtitle, content)
    except Exception:
        pass


if __name__ == '__main__':
    urls = ['http://www.nnrb.com.cn:8080/nnrb/202111{}/html/page_0{}.htm'.format(i, j) for i in range(10, 31) for j in
            range(1, 8)]
    for i in range(1, 10):
        for j in range(1, 8):
            url = 'http://www.nnrb.com.cn:8080/nnrb/2021110{}/html/page_0{}.htm'.format(i, j)
            urls.append(url)
    for url in urls:
        get_url(url)
    for url in g_url:
        get_data(url)
