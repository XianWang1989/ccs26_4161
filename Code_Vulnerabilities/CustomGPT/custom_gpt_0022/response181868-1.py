
import urllib2
from bs4 import BeautifulSoup

# Request the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, "html.parser")

# Find the specific table and all <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.get_text()))

# Print the sorted output
for year_tag in sorted_years:
    print(year_tag)
