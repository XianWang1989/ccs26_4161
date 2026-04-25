
import urllib2
from bs4 import BeautifulSoup

# Request and parse the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the years and sort them
sorted_years = sorted(pub_lv1_parse, key=lambda x: int(x.text))

# Output the sorted years
for year in sorted_years:
    print(year['href'], year.text)
