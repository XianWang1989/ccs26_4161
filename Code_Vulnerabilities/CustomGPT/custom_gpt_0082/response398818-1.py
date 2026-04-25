
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Making the request to the URL
resp = requests.get(url)
# Parsing the response
tree = html.fromstring(resp.content)

# Updating the XPath to correctly select the ticker symbols
tickers = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/a/text()')

# Printing the tickers
print(tickers)
