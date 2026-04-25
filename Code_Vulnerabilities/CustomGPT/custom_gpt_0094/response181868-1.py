
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Fetch and parse the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the desired table and extract the links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags based on the year
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Print the sorted tags
for tag in sorted_years:
    print(tag)
