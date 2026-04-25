
class EspnSpider3(BaseSpider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # Extract player names 
        p_names = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        # Extract player minutes
        p_minutes = hxs.select('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        # Loop through indices of names and minutes
        for index in range(min(len(p_names), len(p_minutes))):
            player_name = p_names[index].strip()
            player_mins = p_minutes[index].strip()
            print(player_name, player_mins)
            yield EspnItem(playerName=player_name, playerMins=player_mins)
