
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)
tree = html.fromstring(resp.content)  # Use .content for binary response

# Update the XPath to correctly target the links in the first column of the table
tickers = tree.xpath('//*[@id="constituents"]/table/tbody/tr/td[1]/a/text()')

print(tickers)
