
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # Initialize item
        item = EspnItem()

        # Extract player names and minutes
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Combine player names and minutes
        for p_name, p_minute in zip(p_names, p_minutes):
            # Create a new item for each player
            item = EspnItem(playerName=p_name, playerMins=p_minute)
            yield item
