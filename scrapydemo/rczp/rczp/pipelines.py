# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json


class RczpPipeline:
    def __init__(self):
        self.fl = open('recp_data.json', 'w')

    def process_item(self, item, spider):
        data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.fl.write(data)
        return item

    def close_spider(self):
        self.fl.close()
