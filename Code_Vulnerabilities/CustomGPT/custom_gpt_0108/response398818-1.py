
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'  # Use HTTPS
resp = requests.get(url)
tree = html.fromstring(resp.content)  # Change to resp.content

# Update XPath to select ticker symbols correctly
tickers = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/a/text()')

print(tickers)
