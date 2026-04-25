
from lxml import html
import requests

# URL of the Wikipedia page containing the S&P 500 companies
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a GET request to the URL
resp = requests.get(url)
# Parse the response text to create an HTML tree
tree = html.fromstring(resp.content)

# Update the XPath to select the ticker symbols from the second column of the table rows
tickers = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
