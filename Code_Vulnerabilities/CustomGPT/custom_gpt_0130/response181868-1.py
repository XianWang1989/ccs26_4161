
import urllib.request
from bs4 import BeautifulSoup

# Fetch and parse the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
sorted_links = sorted(pub_lv1_parse, key=lambda a: int(a.text))

# Display sorted results
for link in sorted_links:
    print(link)
