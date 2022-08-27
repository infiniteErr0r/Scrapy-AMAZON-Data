import scrapy


class SinglewebSpider(scrapy.Spider):
    name = 'singleweb'
    
    def start_requests(self):
        url = 'https://www.amazon.in/LG-Microsoft-Graphics-Thunderbolt4-Warranty/dp/B0B4VKN5J5/ref=sr_1_11_sspa?crid=338VRSV7URB2O&keywords=laptop&qid=1661337537&sprefix=laptop%2Caps%2C223&sr=8-11-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNlFGTlNVOENRSklWJmVuY3J5cHRlZElkPUEwOTUwODQ1M1BDRlRMNDZJN09MQSZlbmNyeXB0ZWRBZElkPUEwNTU0MTcwMUhQRVhGQlBHWkZGMCZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
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