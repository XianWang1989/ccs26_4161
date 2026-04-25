
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        row_items = []

        # Select player rows
        player_rows = hxs.select('//table[@class="mod-data"][1]/tbody/tr')

        for row in player_rows:
            # Extract player name
            player_name = row.select('.//a/text()').extract_first()
            # Extract minutes
            player_mins = row.select('./td[2]/text()').extract_first()

            # Create a new item and append it to the list
            item = EspnItem(playerName=player_name, playerMins=player_mins)
            row_items.append(item)

        # Yield all items at once
        for item in row_items:
            yield item
