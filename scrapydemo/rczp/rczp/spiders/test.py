import requests
from lxml import etree
from bs4 import BeautifulSoup


def print_xpath(eles):
    print(eles)
    # [print(type(x)) for x in eles]
    # [print(etree.tounicode(x)) for x in eles]


url = 'https://www.glrcw.com/job/list/0-0-0-0_0_0_0_0_0_0_0-0-0-0-1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
html = etree.HTML(str(soup))
i = 0
for position in html.xpath('//a[@class="yunjoblist_newname_a"]/text()'):
    print(position)


