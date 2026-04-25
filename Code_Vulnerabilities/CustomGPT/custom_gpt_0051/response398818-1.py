
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)
tree = html.fromstring(resp.content)

# Update the XPath to select all ticker symbols from the first table
tickers = tree.xpath('//table[@class="wikitable"]/tbody/tr/td[1]/a/text()')

# Print the ticker symbols
print(tickers)
