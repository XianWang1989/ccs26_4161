
import urllib.request
from bs4 import BeautifulSoup

# Fetch and parse the HTML
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags based on the year extracted from their text
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Print sorted output
for tag in sorted_tags:
    print(tag)
