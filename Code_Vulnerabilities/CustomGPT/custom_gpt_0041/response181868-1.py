
import urllib.request
from bs4 import BeautifulSoup

# Fetch the HTML content
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract all anchor tags
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Extract years and sort them
sorted_links = sorted(links, key=lambda tag: int(tag.string))

# Print sorted URLs
for link in sorted_links:
    print(link['href'], link.string)
