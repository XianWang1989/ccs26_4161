
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Get the response from the URL
resp = requests.get(url)
# Parse the HTML content
tree = html.fromstring(resp.content)

# Update the XPath to correctly target the ticker symbols
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
