
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from myproject.items import EspnItem  # Adjust the import as needed

class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = Selector(response)

        # Extract player names and minutes in one go
        players = hxs.xpath('//table[@class="mod-data"][1]/tbody/tr')
        for player in players:
            player_name = player.xpath('.//a/text()').get()
            player_minute = player.xpath('.//td[2]/text()').get()

            item = EspnItem()
            item['playerName'] = player_name
            item['playerMins'] = player_minute

            yield item
