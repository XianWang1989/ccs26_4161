
import urllib.request  # use urllib.request for Python 3
from bs4 import BeautifulSoup

# Fetch and parse the content
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and all anchor tags
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.find_all('a')

# Sort the links based on the year (text inside the tag)
sorted_links = sorted(links, key=lambda x: int(x.text))

# Output the sorted links
for link in sorted_links:
    print(link)
