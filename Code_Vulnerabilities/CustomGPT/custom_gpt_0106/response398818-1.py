
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)
tree = html.fromstring(resp.content)

# Adjusted XPath to find all ticker symbols
tickers = tree.xpath('//table[1]//td[1]//a/text()')

print(tickers)
