# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class AmazonwebscrapingPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
        pass
    def process_item(self, item, spider):
        self.hydrate_table(item)
        return item
    def create_connection(self):
        self.con = sqlite3.connect('amazon.db')
        self.curr = self.con.cursor()
        
    def hydrate_table(self, item):
        self.curr.execute(""" INSERT INTO products values (?,?,?,?,?)""",(
        item['name'],
        item['price'],
        item['review'],
        item['availability'],
        item['image_link']
        ))
        self.con.commit()

    def create_table(self):
        self.curr.execute("""
            create table if not exists products(
            product_name text,
            product_price text,
            product_review text,
            product_type text,
            product_imagelink text
            )""")