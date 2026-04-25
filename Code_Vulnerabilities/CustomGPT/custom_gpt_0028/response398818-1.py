
from lxml import html
import requests

# URL of the page to scrape
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Requesting the page content
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Adjusted XPath to extract ticker symbols
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Output the list of tickers
print(tickers)
