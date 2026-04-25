
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        rows = []

        # player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Combine names and minutes
        for p_name, p_minute in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = p_name.strip()
            item['playerMins'] = p_minute.strip()
            yield item
