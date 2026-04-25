
from lxml import html
import requests

# URL to scrape
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the page content
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Adjust the XPath to select all ticker links
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
