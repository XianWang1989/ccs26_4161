
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the page
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Update your XPath expression
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the tickers
print(tickers)
