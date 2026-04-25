
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        # Creating lists to store player names and minutes
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Loop through players and yield a single item for each
        for name, minutes in zip(p_names, p_minutes):
            print(name, minutes)  # for debugging
            yield EspnItem(playerName=name, playerMins=minutes)
