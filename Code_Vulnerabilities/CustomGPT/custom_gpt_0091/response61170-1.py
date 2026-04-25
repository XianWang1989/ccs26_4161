
import scrapy
from scrapy.selector import Selector

class EspnItem(scrapy.Item):
    playerName = scrapy.Field()
    playerMins = scrapy.Field()

class EspnSpider3(scrapy.Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = Selector(response)
        p_names = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        for p_name, p_minute in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = p_name
            item['playerMins'] = p_minute
            yield item
