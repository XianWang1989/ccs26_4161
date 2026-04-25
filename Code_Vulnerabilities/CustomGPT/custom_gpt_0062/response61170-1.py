
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        player_items = []

        # player names 
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]').extract()

        # Combine names and minutes
        for p_name, p_minute in zip(p_names, p_minutes):
            print(f"Name: {p_name}, Minutes: {p_minute}")
            player_items.append(EspnItem(playerName=p_name, playerMins=p_minute))

        # Yield all items at once
        for item in player_items:
            yield item
