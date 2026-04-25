
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Request the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Sort the links by year
sorted_links = sorted(links, key=lambda x: int(x.get_text()))

# Print sorted output
for link in sorted_links:
    print(link)
