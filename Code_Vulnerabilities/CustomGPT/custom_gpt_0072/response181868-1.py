
import urllib2
from bs4 import BeautifulSoup

# Request the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Extract years and sort them
sorted_years = sorted(links, key=lambda tag: int(tag.text))

# Print the sorted years
for link in sorted_years:
    print(link)
