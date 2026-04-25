
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
        for p_name in p_names:
            playerName.append(p_name.strip())  # Collecting names

        # Extract player minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]').extract()
        for p_minute in p_minutes:
            playerMins.append(p_minute.strip())  # Collecting minutes

        # Yield items together
        for name, mins in zip(playerName, playerMins):
            yield EspnItem(playerName=name, playerMins=mins)
