
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

        # Extract player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        playerName.extend(p_names)

        # Extract player minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]').extract()
        playerMins.extend(p_minutes)

        # Yield combined items
        for name, mins in zip(playerName, playerMins):
            item = EspnItem(playerName=name, playerMins=mins)
            yield item
