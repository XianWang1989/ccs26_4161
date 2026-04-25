
from lxml import html
import requests

# URL of the Wikipedia page
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the webpage content
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Corrected XPath to select the ticker symbols
tickers = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
