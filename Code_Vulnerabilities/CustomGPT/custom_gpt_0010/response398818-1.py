
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a GET request
resp = requests.get(url)

# Parse the response text
tree = html.fromstring(resp.content)

# Update the XPath to target the correct table and column
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
