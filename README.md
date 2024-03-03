# Amazon Web Scraping
amazon_product spider searches Amazon and extracts each product's information. The spider will iterate through all pages to extracts product_name, product_price, review, product type fields. The following are the fields the spider scrapes for the Amazon product page:

* Product name
* product price
* Product review
* product type
* product availability

#### Install Guides
Clone this repository into your local machine and make sure you have python installed on it. Once repository has been cloned create a virtual environment and install all the required libraries  and dependencies present in the requirement.txt file. 

### Execution
Activate the virtual environment and execute it by running :
  ```
  scrapy crawl amazon_products

  ```
