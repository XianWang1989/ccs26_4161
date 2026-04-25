
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from your_project.items import EspnItem  # Adjust the import as necessary

class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = Selector(response)
        player_data = []

        # player names
        p_names = hxs.xpath('//table[@class="mod-data"][1]/tbody/tr//a/text()').extract()
        # minutes
        p_minutes = hxs.xpath('//table[@class="mod-data"][1]/tbody/tr/td[2]/text()').extract()

        for name, minutes in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = name.strip()
            item['playerMins'] = minutes.strip()
            yield item
