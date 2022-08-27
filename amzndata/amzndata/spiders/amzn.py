import scrapy


class AmznSpider(scrapy.Spider):
    name = 'amzn'

    def start_requests(self):
        url = 'https://www.amazon.in/s?k=laptop&crid=3BC37O35CKR5C&sprefix=laptop%2Caps%2C238&ref=nb_sb_noss_1'
        
        yield scrapy.Request(url)

    def parse(self, response):
        for lap in response.css('[data-component-type="s-search-result"]'):
            item = {
                'name': lap.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()').get(),
                'stars': lap.xpath('.//span[@class="a-icon-alt"]/text()').get(),
                'price': lap.xpath('.//span[@class="a-price-whole"]/text()').get(),
                'link':'https://www.amazon.in/' + lap.xpath('.//a[@class="a-link-normal s-no-outline"]/@href').get()
            }
            yield item 

        next_page = response.xpath('.//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]/@href').get()
        print('---------------------------------------->'+next_page)
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))