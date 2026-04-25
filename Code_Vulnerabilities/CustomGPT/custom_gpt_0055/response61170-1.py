
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        playerName = []
        playerMins = []

        # player names 
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        playerName.extend(p_names)

        # minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()
        playerMins.extend(p_minutes)

        # Combine player names and minutes in the same item
        for name, mins in zip(playerName, playerMins):
            item = EspnItem(playerName=name, playerMins=mins)
            yield item
