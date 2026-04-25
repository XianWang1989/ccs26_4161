
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)
tree = html.fromstring(resp.content)

# Updated XPath to match the structure
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
