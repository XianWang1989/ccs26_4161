
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the page
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Use the correct XPath to get the ticker symbols
tickers = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/a/text()')

# Print the tickers
print(tickers)
