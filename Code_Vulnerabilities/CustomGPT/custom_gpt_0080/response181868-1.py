
import urllib.request  # Change to urllib for Python 3
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the specific table and extract links
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Sort the links by year
sorted_links = sorted(links, key=lambda a: int(a.get_text()))

# Output the sorted URLs
for link in sorted_links:
    print(link['href'], link.get_text())
