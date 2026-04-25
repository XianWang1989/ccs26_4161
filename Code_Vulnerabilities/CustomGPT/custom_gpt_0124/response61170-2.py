
import scrapy

class EspnItem(scrapy.Item):
    playerName = scrapy.Field()
    playerMins = scrapy.Field()
