
from lxml import html
import requests

# URL to scrape
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the page
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Update XPath to correctly target the ticker links
tickers = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[1]//td[1]/a/text()')

# Print the list of tickers
print(tickers)
