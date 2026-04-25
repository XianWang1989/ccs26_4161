
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from your_project.items import EspnItem

class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        players_data = []  # List to store combined player data

        # player names 
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        # minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Combine player names and minutes in pairs
        for p_name, p_minute in zip(p_names, p_minutes):
            print(f'Player: {p_name}, Minutes: {p_minute}')
            item = EspnItem(playerName=p_name, playerMins=p_minute)
            players_data.append(item)

        # Yield all player data at once
        for player in players_data:
            yield player
