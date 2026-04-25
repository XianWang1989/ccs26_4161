
from lxml import html
import requests

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the content of the page
resp = requests.get(url)

# Parse the content with lxml
tree = html.fromstring(resp.content)

# Use the correct XPath to find the ticker symbols
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
