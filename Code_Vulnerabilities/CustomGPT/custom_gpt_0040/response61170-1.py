
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        player_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        player_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Ensure names and minutes are collected in pairs
        for name, minutes in zip(player_names, player_minutes):
            item = EspnItem(playerName=name.strip(), playerMins=minutes.strip())
            yield item
