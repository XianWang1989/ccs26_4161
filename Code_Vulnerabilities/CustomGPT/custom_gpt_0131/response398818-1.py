
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a GET request to the URL
resp = requests.get(url)

# Parse the response content
tree = html.fromstring(resp.content)

# Adjust XPath to scrape ticker symbols from the first table on the page
tickers = tree.xpath('//table[contains(@class, "wikitable")][1]//td[1]/a/text()')

# Print the list of tickers
print(tickers)
