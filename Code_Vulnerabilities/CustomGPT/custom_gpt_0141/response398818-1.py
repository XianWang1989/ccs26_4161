
from lxml import html
import requests

# URL of the Wikipedia page
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Sending a GET request to the URL
resp = requests.get(url)
# Parsing the HTML content
tree = html.fromstring(resp.content)

# Using the correct XPath to select ticker symbols
# Updated XPath after inspecting the page structure
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Printing the list of tickers
print(tickers)
