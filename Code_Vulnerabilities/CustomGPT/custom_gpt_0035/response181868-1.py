
import urllib2
from bs4 import BeautifulSoup

# Make the request and parse the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract anchor tags
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Sort the links by the year extracted from their text
sorted_links = sorted(links, key=lambda a: int(a.text))

# Output the sorted results
for link in sorted_links:
    print(link)
