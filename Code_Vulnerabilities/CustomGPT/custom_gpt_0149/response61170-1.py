
import scrapy
from scrapy.selector import Selector
from your_project.items import EspnItem  # Adjust the import according to your project structure

class EspnSpider3(scrapy.Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = Selector(response)
        item = EspnItem()

        # Extract player names
        p_names = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        # Extract minutes played
        p_minutes = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Zip the player names and minutes together
        for p_name, p_minute in zip(p_names, p_minutes):
            item['playerName'] = p_name.strip()
            item['playerMins'] = p_minute.strip()
            yield item
