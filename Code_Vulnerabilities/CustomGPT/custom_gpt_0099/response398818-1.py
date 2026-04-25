
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)
tree = html.fromstring(resp.content)

# Using a more reliable XPath to capture all ticker symbols in the first table
tickers = tree.xpath('//table[@class="wikitable"]/tbody/tr/td[1]/text()')

# Cleaning up and printing the list of tickers
tickers = [ticker.strip() for ticker in tickers if ticker.strip()]
print(tickers)
