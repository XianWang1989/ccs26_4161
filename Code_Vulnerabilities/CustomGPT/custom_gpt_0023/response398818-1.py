
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)

# Parse the HTML response
tree = html.fromstring(resp.content)

# Update the XPath to target the correct elements
tickers = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
