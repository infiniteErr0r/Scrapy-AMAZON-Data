import json
import scrapy


class ProductdataSpider(scrapy.Spider):
    name = 'productdata'

    def start_requests(self):
            with open('amzn_py_data.json','r') as f:
                data = f.read()

            data = json.loads(data)

            for i in range(len(data)):
                url = data[i]['link']
                yield scrapy.Request(url)

    def parse(self, response):

        key = response.xpath('//*[@id="productDetails_techSpec_section_1"]//th/text()').extract()
        value = response.xpath('//*[@id="productDetails_techSpec_section_1"]//td/text()').extract()

        data = []
        for i in range(len(key)):
            abc = key[i]+':'+value[i]
            data.append(abc)

        yield{
            'NAME': response.xpath('.//span[@class="a-size-large product-title-word-break"]/text()').get(),
            'RATING': response.xpath('//*[@id="acrPopover"]/@title').get(),
            'PRICE': response.xpath('.//span[@class="a-price-whole"]/text()').get(),  
            'About This Item': response.xpath('//*[@id="feature-bullets"]//li/span/text()').extract(),
            'Technical_Details':data,
            'ASIN':response.xpath('.//*[@id="productDetails_detailBullets_sections1"]//td/text()').get(),
        }