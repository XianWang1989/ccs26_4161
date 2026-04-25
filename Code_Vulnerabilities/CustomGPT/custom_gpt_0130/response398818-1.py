
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Adjusting the XPath to correctly target the ticker symbols
tickers = tree.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr/td[1]/a/text()')

print(tickers)
