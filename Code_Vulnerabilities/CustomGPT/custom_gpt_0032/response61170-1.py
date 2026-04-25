
from scrapy.selector import Selector
from scrapy.spiders import Spider
from myproject.items import EspnItem  # Adjust the import based on your structure

class EspnSpider3(Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = Selector(response)
        p_names = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Make sure the lengths of names and minutes match
        for p_name, p_minute in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = p_name
            item['playerMins'] = p_minute
            yield item
