
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        playerNames = []
        playerMins = []

        # Player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        playerNames.extend(p_names)  # Collect all player names

        # Minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]').extract()
        playerMins.extend(p_minutes)  # Collect all player minutes

        # Yield items aligned correctly
        for name, mins in zip(playerNames, playerMins):
            yield EspnItem(playerName=name, playerMins=mins)
