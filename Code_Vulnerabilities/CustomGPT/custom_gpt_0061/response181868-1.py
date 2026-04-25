
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Make an HTTP request and parse the content
url = "http://www.dummyurl.com"
request = urllib.request.Request(url)
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.find_all('a')

# Sort the list of tags based on the year extracted from href
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag['href'].split('/')[-1]))

# Output the sorted links
for tag in sorted_tags:
    print(tag)
