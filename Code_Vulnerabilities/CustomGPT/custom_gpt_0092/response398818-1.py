
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Request the webpage
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Correct XPath for fetching ticker symbols
tickers = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
