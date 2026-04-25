
from lxml import html
import requests

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Get the page content
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Updated XPath to match the current structure of the page
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
