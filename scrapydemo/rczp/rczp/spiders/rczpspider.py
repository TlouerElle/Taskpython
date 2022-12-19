import scrapy
from lxml import etree
from bs4 import BeautifulSoup
from rczp.items import RczpItem


class RczpspiderSpider(scrapy.Spider):
    name = 'rczpspider'
    allowed_domains = ['https://www.glrcw.com/']
    start_urls = ['https://www.glrcw.com/job/list/0-0-0-0_0_0_0_0_0_0_0-0-0-0-{}.html'.format(x) for x in range(1, 243)]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        html = etree.HTML(str(soup))
        position = [position for position in html.xpath('//a[@class="yunjoblist_newname_a"]/text()')]
        salary = [salary for salary in html.xpath('//div[@class="yunjoblist_newxz"]/text()')]
        company = [company for company in html.xpath('//a[@class="search_job_com_name"]/text()')]
        place = [place for place in html.xpath('//span[@class="search_job_list_box_s"][1]/em[@class="com_search_job_em"]/text()')]
        experience = [experience for experience in html.xpath('//span[@class="search_job_list_box_s"][2]/em[@class="com_search_job_em"]/text()')]
        education = [education for education in html.xpath('//span[@class="search_job_list_box_s"][3]/em[@class="com_search_job_em"]/text()')]
        i = 0
        while i < len(position):
            item = RczpItem()
            item['position'] = position[i]
            item['salary'] = salary[i]
            item['company'] = company[i]
            item['place'] = place [i]
            item['experience'] = experience[i]
            item['education'] = education[i]
            i += 1
            yield item


