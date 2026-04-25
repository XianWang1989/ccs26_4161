
from lxml import html
import requests

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the page content
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Use a more general XPath to find all ticker symbols in the table
tickers = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
