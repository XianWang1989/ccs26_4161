
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        # Selecting the player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # Selecting the minutes played
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Ensure both lists have the same number of entries
        for player_name, player_minute in zip(p_names, p_minutes):
            print(player_name, player_minute)  # This will print them together
            yield EspnItem(playerName=player_name, playerMins=player_minute)
