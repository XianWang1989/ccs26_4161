
import urllib2
from bs4 import BeautifulSoup

# Fetch the web page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)

# Parse the page with BeautifulSoup
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Extract year and sort
sorted_links = sorted(links, key=lambda x: int(x.text))

# Print sorted output
for link in sorted_links:
    print(link)
