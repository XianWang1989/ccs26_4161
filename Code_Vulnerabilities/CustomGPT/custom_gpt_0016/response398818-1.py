
from lxml import html
import requests

# Define the URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the content of the webpage
resp = requests.get(url)

# Parse the content with lxml
tree = html.fromstring(resp.content)

# Use XPath to find all ticker symbols in the table
tickers = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr/td[1]/a/text()')

# Print the extracted tickers
print(tickers)
