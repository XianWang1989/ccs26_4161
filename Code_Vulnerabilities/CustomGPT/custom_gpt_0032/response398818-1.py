
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a request to fetch the page
resp = requests.get(url)
resp.raise_for_status()  # Check for request errors

# Parse the content
tree = html.fromstring(resp.content)

# Use the correct XPath to find tickers in the table
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
