
import urllib.request
from bs4 import BeautifulSoup

# Request the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract all <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the year from each <a> tag and sort them
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Output the sorted years
for tag in sorted_years:
    print(tag)
