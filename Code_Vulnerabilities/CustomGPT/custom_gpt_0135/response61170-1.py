
import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from myproject.items import EspnItem  # Adjust the import according to your project structure

class EspnSpider3(Spider):
    name = "espn3"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        selector = Selector(response)
        players = selector.xpath('//table[@class="mod-data"][1]/tbody/tr')

        for player in players:
            player_name = player.xpath('.//a/text()').get()
            player_mins = player.xpath('./td[2]/text()').get()  # Adjusted to get text correctly

            item = EspnItem(playerName=player_name, playerMins=player_mins)
            yield item
