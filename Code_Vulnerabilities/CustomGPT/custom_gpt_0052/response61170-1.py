
from scrapy.spiders import Spider
from scrapy.selector import Selector
from myproject.items import EspnItem  # Adjust import according to your project structure

class EspnSpider3(Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        sel = Selector(response)
        p_names = sel.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = sel.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Ensure player names and minutes are paired correctly
        for name, minute in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = name.strip()
            item['playerMins'] = minute.strip()
            yield item
