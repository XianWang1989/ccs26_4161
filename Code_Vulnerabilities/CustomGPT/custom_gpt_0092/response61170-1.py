
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []

        # Extract player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        # Extract player minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        for p_name, p_minute in zip(p_names, p_minutes):
            # Create a single item for both name and minutes
            item = EspnItem(playerName=p_name, playerMins=p_minute)
            items.append(item)

        for item in items:
            yield item  # Yield each item to ensure they are processed correctly
