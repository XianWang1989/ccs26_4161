
import urllib.request  # Use urllib instead of urllib2 in Python 3
from bs4 import BeautifulSoup

# Fetch the content
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Extract years and sort them
sorted_years = sorted(links, key=lambda tag: int(tag.text))

# Output sorted URLs
for link in sorted_years:
    print(link)
