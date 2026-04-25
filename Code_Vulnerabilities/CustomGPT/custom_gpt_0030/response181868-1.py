
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Example script to fetch and parse the URLs
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sorting the links by the year extracted from the tags
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Output the sorted results
for tag in sorted_years:
    print(tag, tag['href'])
