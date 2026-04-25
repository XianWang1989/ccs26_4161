
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # Initialize lists to store player names and minutes
        player_data = []

        # Extract player names
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()

        # Extract player minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Combine names and minutes into a single list of items
        for p_name, p_minute in zip(p_names, p_minutes):
            item = EspnItem(playerName=p_name.strip(), playerMins=p_minute.strip())
            player_data.append(item)
            print(f"Player: {p_name.strip()}, Minutes: {p_minute.strip()}")

        # Yield each combined item at once
        for data in player_data:
            yield data
