
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]').extract()

        for p_name, p_minute in zip(p_names, p_minutes):
            player_name = p_name.strip()
            player_minute = p_minute.strip()
            print(player_name, player_minute)
            yield EspnItem(playerName=player_name, playerMins=player_minute)
