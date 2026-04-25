
import urllib.request  # use `urllib.request` in Python 3
from bs4 import BeautifulSoup

# Fetch the page content
request = urllib.request.Request("http://www.dummyurl.com")
with urllib.request.urlopen(request) as response:
    pub_lv1 = response.read()

# Parse the page content with BeautifulSoup
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the list of tags by the text they contain (the years)
sorted_pub_lv1_parse = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Output the sorted list
for tag in sorted_pub_lv1_parse:
    print(tag)
