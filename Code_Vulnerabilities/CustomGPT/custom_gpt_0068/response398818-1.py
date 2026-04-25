
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the webpage
resp = requests.get(url)

# Parse the HTML content
tree = html.fromstring(resp.content)

# Updated XPath to select all ticker elements in the table
tickers = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[1]/a/text()')

print(tickers)
