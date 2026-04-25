
from scrapy.spiders import Spider
from scrapy.selector import Selector

class EspnSpider3(Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = Selector(response)
        # Initialize item list
        items = []

        # Player names
        p_names = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        # Minutes
        p_minutes = hxs.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Check if both lists have the same length
        if len(p_names) == len(p_minutes):
            for p_name, p_minute in zip(p_names, p_minutes):
                # Print player name and minutes for debugging
                print(p_name, p_minute)

                # Create a single item for each player
                item = EspnItem(playerName=p_name, playerMins=p_minute)
                items.append(item)  # Append to items list
                yield item  # Yield the item for output to CSV
        else:
            self.logger.error("Mismatch in the number of players and minutes extracted.")

