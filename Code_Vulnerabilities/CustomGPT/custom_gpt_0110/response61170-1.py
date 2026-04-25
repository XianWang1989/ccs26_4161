
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        # Use HtmlXPathSelector if you're on an older version of Scrapy
        hxs = HtmlXPathSelector(response)
        # Initialize lists for names and minutes
        items = []

        # Extract player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # Extract player minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Combine player names and minutes into items
        for name, minutes in zip(p_names, p_minutes):
            item = EspnItem(playerName=name, playerMins=minutes)
            items.append(item)
            yield item

        # Optionally, yield all items at once (if needed)
        # return items  # This line can be used if you want to return all items at once
