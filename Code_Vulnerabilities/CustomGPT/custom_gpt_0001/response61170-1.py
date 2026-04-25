
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

        # Iterate over both lists and yield a single item for each player
        for p_name, p_minute in zip(p_names, p_minutes):
            print(p_name, p_minute)
            yield EspnItem(playerName=p_name, playerMins=p_minute)
