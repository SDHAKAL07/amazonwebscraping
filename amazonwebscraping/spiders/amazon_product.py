import scrapy
from ..items import AmazonwebscrapingItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon_product'
    page_number = 1
    start_urls = ['https://www.amazon.com/s?k=gaming+headsets&_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&pd_rd_r=85ab8373-90f8-4d5f-acd5-dde77b351a62&pd_rd_w=Tml0P&pd_rd_wg=5bpS0&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=PPGSK898F913AEKRDG5J&qid=1709318088&ref=sr_pg_1']

    def parse(self, response):
        items = AmazonwebscrapingItem()

        product_name = response.css('.a-color-base.a-text-normal ::text').extract()
        product_price = response.css('.a-price .a-offscreen::text').extract()  # Update this selector
        product_review = response.css('.a-icon-alt::text').extract()  # Update this selector
        product_type = response.css('.a-color-state.a-text-bold::text').extract()  # Update this selector
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_review'] = product_review
        items['product_type'] = product_type
        items['product_imagelink'] = product_imagelink

        yield items

        # Increment page number before constructing the next page URL
        self.page_number += 1
        next_page = 'https://www.amazon.com/s?k=gaming+headsets&page=' + str(self.page_number) + '&_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&pd_rd_r=85ab8373-90f8-4d5f-acd5-dde77b351a62&pd_rd_w=Tml0P&pd_rd_wg=5bpS0&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=PPGSK898F913AEKRDG5J&qid=1709309946&ref=sr_pg_2'

        if self.page_number <= 20:
            yield response.follow(next_page)