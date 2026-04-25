
import scrapy
from scrapy.spiders import BaseSpider
from your_project.items import EspnItem  # Adjust the import based on your project structure

class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = scrapy.Selector(response)  # Use scrapy.Selector instead of HtmlXPathSelector
        p_names = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        for name, minutes in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = name.strip()  # Clean whitespace
            item['playerMins'] = minutes.strip()  # Clean whitespace
            yield item  # Yield a single item per player with both fields
