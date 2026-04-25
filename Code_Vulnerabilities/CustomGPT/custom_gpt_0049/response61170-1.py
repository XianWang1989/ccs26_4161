
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # Create a list to hold items temporarily
        items = []

        # player names 
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]').extract()

        # Combine player names and minutes into items and yield them
        for p_name, p_minute in zip(p_names, p_minutes):
            item = EspnItem(playerName=p_name, playerMins=p_minute)
            items.append(item)
            print(f'Player Name: {p_name}, Minutes: {p_minute}')

        # Yield all the gathered items at once
        for item in items:
            yield item
