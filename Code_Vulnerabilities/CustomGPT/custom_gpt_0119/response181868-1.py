
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Fetch and parse the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags by the year in their text
sorted_years = sorted(pub_lv1_parse, key=lambda x: int(x.text))

# Print sorted URLs
for tag in sorted_years:
    print(tag['href'], tag.text)
