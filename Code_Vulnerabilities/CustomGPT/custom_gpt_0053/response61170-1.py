
import scrapy
from scrapy.selector import Selector
from your_project.items import EspnItem  # Adjust import based on your project structure

class EspnSpider3(scrapy.Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        selector = Selector(response)
        players = []

        # player names
        p_names = selector.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # minutes
        p_minutes = selector.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Combine player names and minutes into a list of items
        for name, minute in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = name.strip()
            item['playerMins'] = minute.strip()
            players.append(item)

        # Yield all players as a single output
        for player in players:
            yield player
