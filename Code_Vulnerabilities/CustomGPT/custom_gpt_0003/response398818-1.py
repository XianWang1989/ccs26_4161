
from lxml import html
import requests

# URL for the Wikipedia page of S&P 500 companies
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Sending a GET request to the URL
resp = requests.get(url)

# Parse the HTML response
tree = html.fromstring(resp.content)

# XPath expression to extract ticker symbols from the first table
# Note: It selects all <a> elements within the first table
tickers = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
