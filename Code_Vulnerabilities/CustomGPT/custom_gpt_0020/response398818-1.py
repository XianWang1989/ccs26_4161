
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a request to the website
resp = requests.get(url)
# Parse the HTML content
tree = html.fromstring(resp.content)

# Use a broader XPath to select all tickers in the companies table
tickers = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
