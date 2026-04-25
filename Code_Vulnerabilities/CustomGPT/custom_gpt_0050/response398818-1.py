
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Make a request to the URL
resp = requests.get(url)

# Parse the HTML response
tree = html.fromstring(resp.content)

# Update the XPath to select all ticker symbols from the table
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
