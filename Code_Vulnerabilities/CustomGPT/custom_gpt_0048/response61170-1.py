
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # Initialize a list to hold all items
        items = []

        # player names 
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Zip player names and minutes together
        for p_name, p_minute in zip(p_names, p_minutes):
            print(p_name, p_minute)
            item = EspnItem(playerName=p_name, playerMins=p_minute)
            items.append(item)

        # Yield all items at once
        for item in items:
            yield item
