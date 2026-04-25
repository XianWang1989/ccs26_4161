
from bs4 import BeautifulSoup
import urllib2

# Fetch the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and get all <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Sort the list of tags based on the year extracted from the href attribute
sorted_links = sorted(links, key=lambda tag: int(tag['href'].split('/')[-1]))

# Print sorted links
for link in sorted_links:
    print(link, link['href'])
