
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Update the XPath to reflect the current structure of the Wikipedia page
tickers = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/a/text()')

print(tickers)
