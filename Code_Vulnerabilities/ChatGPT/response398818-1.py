
from lxml import html
import requests

# Set the Wikipedia URL
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a GET request to the URL
resp = requests.get(url)

# Parse the response text
tree = html.fromstring(resp.content)

# Use an XPath expression to select the ticker symbols
# This XPath selects the second column (which contains the tickers) of each row in the table
tickers = tree.xpath('//table[contains(@class, "wikitable")]//tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
