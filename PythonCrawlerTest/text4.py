import requests
from bs4 import BeautifulSoup
import re

urls = set()
count = 0

class crawler_model:
    global urls

    def __init__(self,url, web_name):
        self.url = url
        self.web_name = web_name

    def download_html(self):
        url = self.url
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38 '
        }
        try:
            if url.__contains__('www/http'):
                return None
            response = requests.get(url,headers=headers, timeout=20)
            if response.status_code == 200:
                i = 1
                response.encoding = 'utf-8'
                html = response.text
                return html
            else:
                return None
        except Exception as error:
            print('-'*100)
            print(error)
            print('-' * 100)


    def parser_html(self, html):
        if html is None or html == '':
            return None
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def extraction(self, soup):
        if soup is None or soup == "":
            return None
        data = soup.find_all('a', href=re.compile("^((?!jpg|mailto).)*{}((?!jpg|mailto).)*$".format(self.web_name)))
        for i in data:
            href = i['href']
            if href[0] == "/":
                href = "http:" + href
            if href not in urls:
                urls.add(href)
                self.url = href
                html = self.download_html()
                soup = self.parser_html(html)
                self.extraction(soup)
                print(len(urls), end='    ')
                print(urls)



start_url = 'https://tianqi.2345.com/'
pattern = re.compile('(?<=\.).*(?=\.)')
web_name = pattern.findall(start_url)
if len(web_name) == 1:
    crawler_model = crawler_model(start_url, web_name[0])
    html = crawler_model.download_html()
    soup = crawler_model.parser_html(html)
    crawler_model.extraction(soup)
else:
    print('错误')