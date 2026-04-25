
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Get the content of the page
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Updated XPath to extract ticker symbols
tickers = tree.xpath('//*[@id="mw-content-text"]/table[1]//tbody//tr/td[1]/a/text()')

# Print the extracted tickers
print(tickers)
