
import urllib.request  # Use urllib instead of urllib2 for Python 3
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)

# Parse the page with BeautifulSoup
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(tag.text) for tag in pub_lv1_parse]
years.sort()

# Print sorted years
print(years)

# If you also want to preserve the sorted tags:
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Print sorted tags
for tag in sorted_tags:
    print(tag)
