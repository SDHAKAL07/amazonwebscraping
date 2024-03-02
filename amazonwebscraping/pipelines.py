# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AmazonwebscrapingPipeline:
    def process_item(self, item, spider):
        print("Pipeline :" + item['name'][0])
        print("Pipeline :" + item['price'])
        print("Pipeline :" + item['review'])
        print("Pipeline :" + item['availability'][0])
        print("Pipeline :" + item['image_link'])
        return item
