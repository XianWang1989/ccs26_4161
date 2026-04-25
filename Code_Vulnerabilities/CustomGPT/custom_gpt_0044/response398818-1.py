
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send GET request to the URL
resp = requests.get(url)
# Parse the response text
tree = html.fromstring(resp.content)

# Update the XPath to get all ticker links
tickers = tree.xpath('//*[@id="mw-content-text"]/table[1]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
