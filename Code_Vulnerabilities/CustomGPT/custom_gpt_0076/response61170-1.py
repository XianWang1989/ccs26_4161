
from scrapy.spiders import Spider
from scrapy.selector import Selector
from your_project.items import EspnItem

class EspnSpider3(Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = Selector(response)
        player_names = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        player_minutes = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        for name, minutes in zip(player_names, player_minutes):
            item = EspnItem()
            item['playerName'] = name
            item['playerMins'] = minutes
            yield item
