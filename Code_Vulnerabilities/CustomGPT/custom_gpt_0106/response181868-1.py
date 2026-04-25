
import urllib.request  # Change to urllib for Python 3
from bs4 import BeautifulSoup

# Request the page and parse it
request = urllib.request.Request("http://www.dummyurl.com")  # Use urllib.request in Python 3
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags by extracting year from href
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag['href'].split('/')[-1]))

# Print sorted output
for tag in sorted_tags:
    print(tag)
