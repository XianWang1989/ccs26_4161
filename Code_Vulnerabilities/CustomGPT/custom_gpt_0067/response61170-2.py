
from scrapy import Item, Field

class EspnItem(Item):
    playerName = Field()
    playerMins = Field()
