
from scrapy import Spider
from scrapy.selector import Selector

class EspnItem(scrapy.Item):
    playerName = scrapy.Field()
    playerMins = scrapy.Field()

class EspnSpider3(Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        sel = Selector(response)

        # Get player names and minutes
        p_names = sel.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = sel.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Ensure both lists have the same length
        for name, mins in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = name.strip()
            item['playerMins'] = mins.strip()
            yield item
