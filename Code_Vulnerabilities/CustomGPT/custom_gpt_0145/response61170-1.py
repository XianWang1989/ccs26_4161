
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        players = []

        # player names 
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # combining names and minutes
        for name, mins in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = name.strip()  # ensure no extra spaces
            item['playerMins'] = mins.strip()  # ensure no extra spaces
            players.append(item)

        # now yield all items
        for player in players:
            yield player
