
import urllib.request  # Updated for Python 3
from bs4 import BeautifulSoup

# Fetch and parse the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
year_tags = pub_lv1_parse.findAll('a')

# Extract years and sort them
sorted_years = sorted(year_tags, key=lambda tag: int(tag.text))

# Display sorted years
for tag in sorted_years:
    print(tag)
