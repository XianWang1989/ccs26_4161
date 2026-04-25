
import urllib2
from bs4 import BeautifulSoup

# Make the request and parse the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the links based on the year extracted from the tag text
sorted_links = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Output the sorted links
for link in sorted_links:
    print(link)
