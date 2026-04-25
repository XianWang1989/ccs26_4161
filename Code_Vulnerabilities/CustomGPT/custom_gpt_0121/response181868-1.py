
import urllib2
from bs4 import BeautifulSoup

# Sample request to retrieve the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the years and sort them
sorted_years = sorted(pub_lv1_parse, key=lambda a: int(a.text))

# Output the sorted result
for tag in sorted_years:
    print(tag)
