
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # Initialize lists to hold player names and minutes
        player_items = []

        # Player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # Player minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Combine names and minutes into a list of items
        for p_name, p_minute in zip(p_names, p_minutes):
            item = EspnItem(playerName=p_name, playerMins=p_minute)
            player_items.append(item)
            yield item

        # Optionally: Yield all items at once (for example, if you were collecting data for further processing)
        # yield player_items
