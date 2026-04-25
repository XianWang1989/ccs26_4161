
import urllib.request
from bs4 import BeautifulSoup

# Request the URL and parse the HTML
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract all <a> tags
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Sort the links based on the year extracted from the tag text
sorted_links = sorted(links, key=lambda tag: int(tag.text))

# Print sorted URLs
for link in sorted_links:
    print(link['href'], link.text)
