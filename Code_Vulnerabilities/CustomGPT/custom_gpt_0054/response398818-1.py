
from lxml import html
import requests

# URL to scrape
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Get the page content
resp = requests.get(url)

# Parse the HTML content
tree = html.fromstring(resp.content)

# Modified XPath to select all tickers in the first table
# You may need to adjust the [1] based on table structure.
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the tickers
print(tickers)
