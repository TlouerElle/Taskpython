from urllib.request import urlretrieve
import requests
from lxml import etree


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
            print(str(count) + '  img')
            urlretrieve(url, './img/{}'.format(imgname))
            count += 1
    except Exception as er:
        download(url)


if __name__ == '__main__':
    urls = ['https://www.vcg.com/creative-image/laji/?page={}'.format(i) for i in range(1, 100)]
    for url in urls:
        print(url)
        download(url)
