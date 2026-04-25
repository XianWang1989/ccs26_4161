
import scrapy
from scrapy.selector import Selector
from yourproject.items import EspnItem  # Update with your actual items module

class EspnSpider3(scrapy.Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        selector = Selector(response)
        rows = []
        playerNames = selector.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        playerMins = selector.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Zip player names and minutes together to create items
        for name, mins in zip(playerNames, playerMins):
            item = EspnItem()
            item['playerName'] = name.strip()
            item['playerMins'] = mins.strip()
            yield item
