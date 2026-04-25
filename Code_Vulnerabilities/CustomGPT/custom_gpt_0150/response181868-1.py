
import urllib.request  # For Python 3
from bs4 import BeautifulSoup

# Request and parse the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
sorted_years = sorted(pub_lv1_parse, key=lambda x: int(x.text))

# Output the sorted list
for tag in sorted_years:
    print(tag)
