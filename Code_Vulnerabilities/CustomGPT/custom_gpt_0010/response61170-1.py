
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        for i in range(len(p_names)):
            player_item = EspnItem(
                playerName=p_names[i],
                playerMins=p_minutes[i] if i < len(p_minutes) else None  # Handles unequal lengths
            )
            print(player_item)  # Debugging output
            yield player_item
