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
        if  item['product_name'][0]:
            self.curr.execute(""" INSERT INTO products VALUES (?,?,?,?,?)""",(
                item['product_name'][0],
                item['product_price'][0],
                item['product_review'][0],
                item['product_type'][0],
                item['product_imagelink'][0]
            ))
            self.con.commit()
        return item

    def create_table(self):
        self.curr.execute("""
            CREATE TABLE IF NOT EXISTS products(
            product_name TEXT,
            product_price TEXT,
            product_review TEXT,
            product_type TEXT,
            product_imagelink TEXT
            )""")