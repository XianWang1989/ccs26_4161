
from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from your_project.items import EspnItem  # Adjust to your actual item import

class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        selector = Selector(response)
        p_names = selector.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = selector.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        for p_name, p_minute in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = p_name.strip()  # Remove any extra whitespace
            item['playerMins'] = p_minute.strip()  # Remove any extra whitespace
            yield item
