
from lxml import html
import requests

# URL of the Wikipedia page
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a GET request to the URL
resp = requests.get(url)

# Parse the HTML content
tree = html.fromstring(resp.content)

# Update the XPath to capture the tickers correctly
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
