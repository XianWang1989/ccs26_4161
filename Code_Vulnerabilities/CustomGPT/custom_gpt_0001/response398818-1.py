
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)
tree = html.fromstring(resp.content)

# Updated XPath to select all ticker symbols in the first table
tickers = tree.xpath('//*[@id="mw-content-text"]/table[1]//td[1]/a/text()')

# Print the extracted tickers
print(tickers)
