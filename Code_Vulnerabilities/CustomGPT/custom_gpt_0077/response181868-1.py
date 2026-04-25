
import urllib.request  # use this instead of urllib2 in Python 3
from bs4 import BeautifulSoup

# Make a request to the URL
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract all anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
link_tags = pub_lv1_parse.findAll('a')

# Sort the tags
sorted_links = sorted(link_tags, key=lambda tag: int(tag.get_text()))

# Output the sorted links
for link in sorted_links:
    print(link)
