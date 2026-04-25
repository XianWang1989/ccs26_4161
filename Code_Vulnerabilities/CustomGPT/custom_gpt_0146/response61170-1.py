
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        # Use the same item for player names and minutes
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Ensure that player names and minutes line up in terms of their index
        for name, minute in zip(p_names, p_minutes):
            # Yield a single item with both name and minute
            yield EspnItem(playerName=name, playerMins=minute)

