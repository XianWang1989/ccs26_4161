
import urllib.request  # use urllib.request for Python 3
from bs4 import BeautifulSoup

# Request the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)

# Parse the webpage
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the list of tags by extracting the year from the text
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Output the sorted result
for tag in sorted_years:
    print(tag)
