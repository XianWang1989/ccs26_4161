
from lxml import html
import requests

# URL of the Wikipedia page
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a GET request to the URL
resp = requests.get(url)

# Parse the response text using lxml
tree = html.fromstring(resp.content)

# Use a more general XPath to get all the ticker symbols
tickers = tree.xpath('//*[@id="mw-content-text"]/table[1]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
