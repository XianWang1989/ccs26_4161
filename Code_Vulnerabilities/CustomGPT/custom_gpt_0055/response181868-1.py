
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the specific table and extract links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags based on the year (text content)
sorted_links = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Print the sorted URLs
for link in sorted_links:
    print(link['href'], link.text)
