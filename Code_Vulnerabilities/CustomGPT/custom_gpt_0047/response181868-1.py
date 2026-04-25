
import urllib2
from bs4 import BeautifulSoup

# Fetching the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Finding the table and extracting anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extracting years and sorting
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Displaying sorted output
for tag in sorted_years:
    print(tag)
