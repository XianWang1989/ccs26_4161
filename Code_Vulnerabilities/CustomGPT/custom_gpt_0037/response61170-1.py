
import scrapy
from scrapy.selector import Selector

class EspnSpider3(scrapy.Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        selector = Selector(response)
        players = []

        # Extract player names and minutes
        p_names = selector.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = selector.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Combine player names and minutes into items
        for name, minutes in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = name.strip()
            item['playerMins'] = minutes.strip()
            players.append(item)
            yield item  # Yield the item

        # Optionally, you can log the output if needed
        for player in players:
            self.log(f"Player: {player['playerName']}, Minutes: {player['playerMins']}")
