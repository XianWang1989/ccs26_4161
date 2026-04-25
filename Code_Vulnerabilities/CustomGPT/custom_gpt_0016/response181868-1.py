
import urllib.request  # For Python 3, use urllib.request instead of urllib2
from bs4 import BeautifulSoup

# Make the request and parse the content
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table containing the links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extracting and sorting the year from the tags' text
sorted_links = sorted(pub_lv1_parse, key=lambda x: int(x.text))

# Print the sorted tags
for link in sorted_links:
    print(link)
