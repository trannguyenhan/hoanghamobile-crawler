import scrapy

from hoanghamobilecrawler.items import HoanghamobilecrawlerItem


class SmartphoneSpider(scrapy.Spider):
    name = 'smartphone'
    MAX_PAGE = 10
    page_url = "https://hoanghamobile.com"
    base_url = 'https://hoanghamobile.com/dien-thoai-di-dong'

    def start_requests(self):
        url = self.base_url + "?page=" + str(self.MAX_PAGE)
        yield scrapy.Request(url=url, callback=self.parse_link)

    def parse_link(self, response):
        links = response.css(".col-content").css(".item .img").css("a").xpath("@href").extract()
        for link in links: 
            link_tmp = self.page_url + link
            yield scrapy.Request(url=link_tmp, callback=self.parse, meta={"request_url": link_tmp})

    def parse(self, response):
        url = response.meta.get("request_url")
        name = None
        
        ele_name = response.css(".top-product h1::text").extract()
        if len(ele_name) > 1: 
            name = ele_name[1].replace("\r", "").replace("\n", "").replace("\t", "")
        else: 
            name = ele_name[0].replace("\r", "").replace("\n", "").replace("\t", "")

        cpu = None
        ram = None
        rom = None
        pin = None

        eles = response.css(".product-right .specs-special ol li")
        for ele in eles: 
            strong = ele.css("strong::text").extract_first()
            span = ele.css("span::text").extract_first()
            
            if "CPU" in strong: 
                cpu = span
            if "RAM" in strong: 
                ram = span
            if "ROM" in strong: 
                rom = span
            if "pin" in strong: 
                pin = span
        
        eles = response.css("#colorOptions").css(".item")
        for ele in eles: 
            color = ele.css("span label strong::text").extract_first()
            price = ele.css("span + strong::text").extract_first()

            item = HoanghamobilecrawlerItem()
            item['url'] = url
            item['name'] = name
            item['cpu'] = cpu
            item['ram'] = ram
            item['rom'] = rom
            item['pin'] = pin
            item['color'] = color
            item['price'] = price

            yield item
