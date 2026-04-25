
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Get the webpage
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Use the correct XPath to find tickers
tickers = tree.xpath('//table[1]//tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
