
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
resp = requests.get(url)

# Parse the response text
tree = html.fromstring(resp.content)

# Use a corrected XPath to grab the ticker symbols
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/text()')

# Print the tickers
print(tickers)
