
import urllib2
from bs4 import BeautifulSoup

# Fetching the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Finding the specific table and extracting links
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Extracting the years from the tags and sorting them
sorted_links = sorted(links, key=lambda x: int(x.text))

# Printing the sorted result
for link in sorted_links:
    print(link, link['href'])
