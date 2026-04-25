
import urllib2
from bs4 import BeautifulSoup

# Fetch and parse the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the desired table and extract links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the list of tags by their year (the text within each <a> tag)
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Output the sorted list
for tag in sorted_years:
    print(tag['href'], tag.text)
