
from lxml import html
import requests

# URL of the Wikipedia page
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the page
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Updated XPath to get tickers
tickers = tree.xpath('//table[@class="wikitable"]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
