
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the content of the webpage
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Correct XPath to extract ticker symbols
tickers = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
