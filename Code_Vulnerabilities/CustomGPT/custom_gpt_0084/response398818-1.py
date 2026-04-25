
from lxml import html
import requests

# URL to scrape
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Sending a GET request to the URL
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Using a revised XPath to get all ticker symbols
tickers = tree.xpath('//table[1]//tbody//tr/td[1]/a/text()')

# Printing the list of tickers
print(tickers)
