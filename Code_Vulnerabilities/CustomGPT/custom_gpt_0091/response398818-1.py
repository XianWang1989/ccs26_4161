
from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Make a request to the webpage
resp = requests.get(url)
tree = html.fromstring(resp.content)  # Use resp.content instead of resp.text for better handling

# Update the XPath to target the correct anchor tags within the first table
tickers = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
