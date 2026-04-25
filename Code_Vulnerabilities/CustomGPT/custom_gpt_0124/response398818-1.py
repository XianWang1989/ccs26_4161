
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Make a request to the webpage
resp = requests.get(url)
tree = html.fromstring(resp.content)  # Use resp.content to avoid issues with encoding

# Update the XPath to fetch the ticker symbols
tickers = tree.xpath('//table[contains(@class, "wikitable")][1]//td[1]//text()')

# Clean up the ticker symbols by stripping whitespace and filtering empty strings
tickers = [ticker.strip() for ticker in tickers if ticker.strip()]

print(tickers)
