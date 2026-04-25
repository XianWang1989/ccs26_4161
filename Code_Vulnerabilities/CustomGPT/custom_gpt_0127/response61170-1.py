
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # Create a list to store all items
        items = []

        # player names 
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]').extract()

        # Combine names and minutes into items
        for p_name, p_minute in zip(p_names, p_minutes):
            item = EspnItem(playerName=p_name.strip(), playerMins=p_minute.strip())
            items.append(item)

        # Yield all items at once
        for item in items:
            yield item
