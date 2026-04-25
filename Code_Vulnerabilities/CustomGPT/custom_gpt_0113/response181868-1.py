
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Fetch the page
url = "http://www.dummyurl.com"
request = urllib.request.Request(url)
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the specific table and extract anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_links = pub_lv1_parse.findAll('a')

# Sort the tags by the year extracted from the href attribute
sorted_links = sorted(pub_lv1_links, key=lambda tag: int(tag.get('href').split('/')[-1]))

# Output the sorted results
for link in sorted_links:
    print(link)
