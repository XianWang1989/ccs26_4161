
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()  # Ensure to extract text here

        # Check if the number of players and minutes match
        if len(p_names) != len(p_minutes):
            self.logger.warning("Mismatch between player names and minutes count")

        # Loop to create items for player names and minutes together
        for p_name, p_minute in zip(p_names, p_minutes):
            print(f"Name: {p_name}, Minutes: {p_minute}")
            yield EspnItem(playerName=p_name, playerMins=p_minute)

