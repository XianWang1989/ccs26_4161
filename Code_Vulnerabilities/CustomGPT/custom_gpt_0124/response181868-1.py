
import urllib.request  # Use this for Python 3
from bs4 import BeautifulSoup

# Fetch the page
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract the links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the list of tags based on the year
sorted_links = sorted(pub_lv1_parse, key=lambda x: int(x.text))

# Output the sorted links
for link in sorted_links:
    print(link)
