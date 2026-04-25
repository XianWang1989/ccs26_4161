
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Make the request to the URL
resp = requests.get(url)

# Parse the content of the page
tree = html.fromstring(resp.content)

# Use a more general XPath to get all ticker symbols from the table
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the extracted tickers
print(tickers)
