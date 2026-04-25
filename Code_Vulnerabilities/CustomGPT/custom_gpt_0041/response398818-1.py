
from lxml import html
import requests

# URL of the Wikipedia page
url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Get the response from the URL
resp = requests.get(url)

# Parse the content with lxml
tree = html.fromstring(resp.content)

# Update XPath to extract tickers. The first 'td' in each row corresponds to the ticker symbol.
tickers = tree.xpath('//table[@class="wikitable"]/tbody/tr/td[1]/a/text()')

# Print the list of tickers
print(tickers)
