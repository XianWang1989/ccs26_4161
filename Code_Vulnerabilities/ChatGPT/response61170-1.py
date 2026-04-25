
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        player_items = []

        # Player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # Minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Ensure that we don't exceed the length of the shorter list
        for p_name, p_minute in zip(p_names, p_minutes):
            item = EspnItem()
            item['playerName'] = p_name.strip()  # Remove whitespace if any
            item['playerMins'] = p_minute.strip()  # Remove whitespace if any

            # Store the item in a list before yielding (optional)
            player_items.append(item)

            # Yield the single complete item
            yield item

        # If you want to log or print the player items, you can do it here:
        for player_item in player_items:
            print(player_item)
