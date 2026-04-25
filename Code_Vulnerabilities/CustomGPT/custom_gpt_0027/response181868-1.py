
import urllib2
from bs4 import BeautifulSoup

# Request the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the specific table and all 'a' tags within it
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Extract year and sort
sorted_links = sorted(links, key=lambda tag: int(tag.get_text()))

# Print sorted output
for link in sorted_links:
    print(link)
