
from lxml import html
import requests

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Request the webpage
resp = requests.get(url)

# Parse the HTML content
tree = html.fromstring(resp.content)

# Adjusted XPath to extract all ticker symbols from the first table
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
