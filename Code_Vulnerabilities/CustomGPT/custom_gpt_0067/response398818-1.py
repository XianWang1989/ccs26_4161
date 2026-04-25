
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)
tree = html.fromstring(resp.content)

# Adjusted XPath expression to get all ticker symbols from the table
tickers = tree.xpath('//*[@id="mw-content-text"]/table[1]/tbody/tr/td[1]/a/text()')

print(tickers)
