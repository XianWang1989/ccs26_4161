
from lxml import html
import requests

# URL of the Wikipedia page
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the page
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Adjusted XPath to select all ticker symbols from the table
tickers = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[1]//td[1]/text()')

# Clean the list by stripping whitespace
tickers = [ticker.strip() for ticker in tickers if ticker.strip()]

print(tickers)
