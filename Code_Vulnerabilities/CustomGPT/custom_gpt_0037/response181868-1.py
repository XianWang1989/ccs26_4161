
import urllib.request
from bs4 import BeautifulSoup

# Fetch content from the URL
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_links = pub_lv1_parse.find_all('a')

# Sort the links based on the year
sorted_links = sorted(pub_lv1_links, key=lambda x: int(x.text))

# Print the sorted links
for link in sorted_links:
    print(link)
