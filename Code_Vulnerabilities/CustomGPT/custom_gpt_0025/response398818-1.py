
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the content from the URL
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Updated XPath to select all ticker symbols in the first table body
tickers = tree.xpath('//*[@id="mw-content-text"]/table[1]//tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
