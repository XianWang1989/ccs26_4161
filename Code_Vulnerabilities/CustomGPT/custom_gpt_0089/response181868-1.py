
import urllib2
from bs4 import BeautifulSoup

# Fetch the page and parse it
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Locate the table and extract the anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags by the year extracted from their text
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Print the sorted URLs
for tag in sorted_tags:
    print(tag['href'], tag.text)
