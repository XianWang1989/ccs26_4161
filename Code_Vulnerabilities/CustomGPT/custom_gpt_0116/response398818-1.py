
from lxml import html
import requests

# URL of the Wikipedia page
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Make a request to the website
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Adjust XPath to capture all ticker links
tickers = tree.xpath('//*[@id="constituents"]/table/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
