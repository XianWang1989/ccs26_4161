
from lxml import html
import requests

# URL of the webpage to scrape
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Sending the GET request to fetch the page
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Correct XPath to select ticker symbols
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Output the list of tickers
print(tickers)
