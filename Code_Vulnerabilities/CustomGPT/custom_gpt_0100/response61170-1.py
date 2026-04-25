
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        # Select player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # Select minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Ensure that both lists have the same length
        for p_name, p_minute in zip(p_names, p_minutes):
            print(p_name, p_minute)  # Debugging print
            yield EspnItem(playerName=p_name.strip(), playerMins=p_minute.strip())
