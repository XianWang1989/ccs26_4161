
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)
tree = html.fromstring(resp.content)  # Use resp.content for bytes

# Adjusted XPath to select the ticker symbols
tickers = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[1]/a/text()')

print(tickers)
