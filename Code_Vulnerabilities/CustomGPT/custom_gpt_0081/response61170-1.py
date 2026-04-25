
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item = EspnItem()

        # player names 
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]').extract()

        # Make sure to yield both player names and their corresponding minutes together
        for p_name, p_minute in zip(p_names, p_minutes):
            player_name = p_name.strip()  # Clean up the player name
            player_minute = p_minute.strip()  # Clean up the player minute

            print(player_name, player_minute)  # Optional: print for debugging

            yield EspnItem(playerName=player_name, playerMins=player_minute)
