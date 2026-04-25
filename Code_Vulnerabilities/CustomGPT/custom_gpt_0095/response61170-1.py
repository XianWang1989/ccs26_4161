
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        # Initialize lists to store player data
        players = []

        # Extract player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # Extract player minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Combine names and minutes into items
        for p_name, p_minute in zip(p_names, p_minutes):
            print(p_name, p_minute)  # Output for debugging
            item = EspnItem(playerName=p_name, playerMins=p_minute)
            players.append(item)
            yield item  # Yielding a combined item

# Ensure your EspnItem is defined correctly with both fields:
class EspnItem(scrapy.Item):
    playerName = scrapy.Field()
    playerMins = scrapy.Field()
