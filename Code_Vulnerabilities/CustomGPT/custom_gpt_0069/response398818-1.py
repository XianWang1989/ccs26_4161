
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)
tree = html.fromstring(resp.content)

# Update your XPath to capture all the ticker symbols in the first table
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/text()')

# Clean up and remove any leading/trailing whitespace
tickers = [ticker.strip() for ticker in tickers if ticker.strip()]

print(tickers)
