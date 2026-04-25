
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)
tree = html.fromstring(resp.content)

# Updated XPath to correctly select the tickers
tickers = tree.xpath('//table[@class="wikitable"]/tbody/tr/td[1]/a/text()')

print(tickers)
