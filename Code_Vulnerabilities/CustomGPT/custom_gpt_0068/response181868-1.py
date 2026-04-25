
import urllib2
from bs4 import BeautifulSoup

# Fetch the content
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)

# Parse the HTML
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})

# Find all 'a' tags
pub_lv1_links = pub_lv1_table.findAll('a')

# Sort the links based on the year
sorted_links = sorted(pub_lv1_links, key=lambda x: int(x.text))

# Display sorted URLs
for link in sorted_links:
    print(link['href'], link.text)
