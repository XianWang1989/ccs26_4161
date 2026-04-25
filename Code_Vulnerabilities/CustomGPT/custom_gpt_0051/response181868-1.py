
import urllib.request  # Use urllib.request instead of urllib2 in Python 3
from bs4 import BeautifulSoup

# Make the request
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)

# Parse the response
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Sort links by year
sorted_links = sorted(links, key=lambda x: int(x.text))

# Print sorted results
for link in sorted_links:
    print(link)
