
import scrapy

class EspnSpider3(scrapy.Spider):
    name = "espn3.org"
    allowed_domains = ["espn3.org"]
    start_urls = [
        "http://scores.espn.go.com/nba/boxscore?gameId=310502004"
    ]

    def parse(self, response):
        p_names = response.xpath('(//table[@class="mod-data"][1]/tbody/tr)//a/text()').extract()
        p_minutes = response.xpath('(//table[@class="mod-data"][1]/tbody/tr)/td[2]/text()').extract()

        for player_name, player_min in zip(p_names, p_minutes):
            yield {
                'playerName': player_name.strip(),
                'playerMins': player_min.strip()
            }
