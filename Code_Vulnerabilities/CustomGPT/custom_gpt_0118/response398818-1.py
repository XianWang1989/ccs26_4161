
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send the request to the URL
resp = requests.get(url)
# Parse the response text
tree = html.fromstring(resp.content)

# Use the correct XPath to select the ticker symbols
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
