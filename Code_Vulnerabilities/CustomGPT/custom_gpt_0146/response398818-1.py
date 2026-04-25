
from lxml import html
import requests

# URL of the Wikipedia page
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Sending a GET request to fetch the content of the page
resp = requests.get(url)

# Parsing the content with lxml
tree = html.fromstring(resp.content)

# Using XPath to select ticker symbols from the first table
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Printing the list of tickers
print(tickers)
