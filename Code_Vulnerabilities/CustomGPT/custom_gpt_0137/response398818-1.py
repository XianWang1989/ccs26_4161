
from lxml import html
import requests

# URL of the webpage to scrape
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetching the content of the webpage
resp = requests.get(url)
tree = html.fromstring(resp.text)

# Adjusted XPath to select all the ticker symbols from the table
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
