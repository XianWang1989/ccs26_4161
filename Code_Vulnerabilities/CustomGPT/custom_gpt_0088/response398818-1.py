
from lxml import html
import requests

url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

resp = requests.get(url)

# Check if the request was successful
if resp.status_code == 200:
    tree = html.fromstring(resp.content)

    # Adjusted XPath to correctly select the ticker symbols
    tickers = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[1]/a/text()')

    print(tickers)
else:
    print("Failed to retrieve the webpage.")
