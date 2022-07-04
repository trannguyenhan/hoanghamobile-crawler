from scrapy.crawler     import CrawlerProcess
from scrapy.settings import Settings
from hoanghamobilecrawler.spiders.smartphone import SmartphoneSpider

setting = Settings()
setting.setmodule('hoanghamobilecrawler.settings', priority='project')

process = CrawlerProcess(settings=setting)
process.crawl(SmartphoneSpider)
process.start()