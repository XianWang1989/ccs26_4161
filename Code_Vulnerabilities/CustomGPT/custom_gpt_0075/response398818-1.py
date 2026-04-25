
from lxml import html
import requests

# Define the URL
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a GET request to fetch the webpage content
resp = requests.get(url)
tree = html.fromstring(resp.content)

# Use a more generalized XPath
tickers = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[1]/a/text()')

# Output the list of tickers
print(tickers)
