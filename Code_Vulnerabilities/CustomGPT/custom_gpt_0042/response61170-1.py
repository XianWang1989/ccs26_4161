
from scrapy.spiders import Spider
from scrapy.selector import Selector
from myproject.items import EspnItem  # make sure to import your item class

class EspnSpider3(Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = Selector(response)
        players = []

        # Extract player names
        p_names = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # Extract player minutes
        p_minutes = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Combine names and minutes into a list of items
        for p_name, p_minute in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = p_name
            item['playerMins'] = p_minute
            players.append(item)

        # Yielding all items at once
        for player in players:
            yield player
