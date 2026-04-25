
from bs4 import BeautifulSoup
import urllib.request  # Use urllib.request for Python 3

# Fetch and parse the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract the links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Extract years and sort them
sorted_links = sorted(links, key=lambda a: int(a.text))

# Output the sorted list
for link in sorted_links:
    print(link)
