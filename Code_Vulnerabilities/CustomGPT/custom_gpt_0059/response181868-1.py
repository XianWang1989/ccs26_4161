
from bs4 import BeautifulSoup
import urllib2

# Fetch the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1)

# Find the table and the anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Sort the links based on the year in the text
sorted_links = sorted(links, key=lambda x: int(x.text))

# Print the sorted output
for link in sorted_links:
    print(link)
