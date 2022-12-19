import requests
import csv
import random
from lxml import etree
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

count = 1979
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
ip_list = []
f = open(r'D:\pythonProject\crawler_project\ip.txt', 'r')
for ip in f.readlines():
    ip = ip.strip()
    ip_list.append(ip)


def download_html(url):
    try:
        ip = random.choice(ip_list)
        proxies = {'https': ip}
        print(proxies)
        response = requests.get(url, header, proxies=proxies, timeout=20, stream=True, verify=False)
        if response.status_code != 200:
            print(response.status_code)
            return
        return response.text
    except Exception as er:
        print(er)



def get_data(html):
    try:
        first_html = etree.HTML(html)
        second_url = first_html.xpath('//*/header/h1/a/@href')
        global count
        for url in second_url:
            print('Currently write {} data'.format(count))
            second_html = download_html(url)
            second_html = etree.HTML(second_html)
            title = second_html.xpath('//h1[@class="entry-title"]/text()')[0]
            content_list = second_html.xpath('//article/div/p[1]/text()')
            content = ''
            for i in content_list:
                content = content + str(i)
            star = second_html.xpath('//strong[2]/text()')[0]
            about = second_html.xpath('//p[2]/a/text()')
            time = second_html.xpath('//time[@class="entry-date"]/text()')[0]
            classification_list = second_html.xpath('//footer[@class="entry-meta"]/a/text()')
            classification = ''
            for i in classification_list:
                classification = classification + str(',' + i)
            author = second_html.xpath('//a[@class="url fn n"]/text()')[0]
            with open(r'funny_data.csv', 'a+', encoding='utf-8') as f:
                row = [title, content, star, about, time, classification, author]
                writer = csv.writer(f)
                writer.writerow(row)
            count += 1
            print('---------->finish<----------')
    except Exception as er:
        print(er)


if __name__ == '__main__':
    first_urls = ['https://youquhome.com/page/{}/'.format(i) for i in range(198, 202)]
    for url in first_urls:
        html = download_html(url)
        download_html(url)
        get_data(html)
