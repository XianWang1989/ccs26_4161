
import urllib2
from bs4 import BeautifulSoup

request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sorting the tags by extracting the year as an integer
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Printing sorted results
for year in sorted_years:
    print(year)
