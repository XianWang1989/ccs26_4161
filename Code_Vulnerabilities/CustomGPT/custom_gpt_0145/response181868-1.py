
from bs4 import BeautifulSoup
import urllib.request  # Use urllib.request instead of urllib2 in Python 3

# Example request to fetch data
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the specific table and extract the anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extracting years from the href attribute and sorting
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag['href'].split('/')[-1]))

# Output the sorted list
for tag in sorted_years:
    print(tag)
