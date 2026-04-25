
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        player_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        player_mins = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        for p_name, p_minute in zip(player_names, player_mins):
            item = EspnItem(playerName=p_name, playerMins=p_minute)
            yield item
