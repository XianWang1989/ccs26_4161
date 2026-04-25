
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Requesting the page
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Finding the relevant table and extracting the links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sorting the tags based on the year text
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Printing the sorted results
for tag in sorted_tags:
    print(tag)  # or print(tag['href']) to print only links
