
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # Create lists to hold player names and minutes
        playerName = []
        playerMins = []

        # player names 
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        playerName.extend(p_names)  # Extend the playerName list with names

        # minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]').extract()
        playerMins.extend(p_minutes)  # Extend the playerMins list with minutes

        # Yield items combining names and minutes
        for name, mins in zip(playerName, playerMins):
            item = EspnItem(playerName=name, playerMins=mins)
            yield item
