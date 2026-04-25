
import urllib.request
from bs4 import BeautifulSoup

# Fetch the page
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract the anchors
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags based on the year extracted from the href
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag['href'].split('/')[-1]))

# Print the sorted output
for tag in sorted_years:
    print(tag)
