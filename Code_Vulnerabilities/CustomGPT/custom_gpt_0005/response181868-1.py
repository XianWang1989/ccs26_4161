
import urllib2
from bs4 import BeautifulSoup

# Requesting the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Finding the desired table and extracting the tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extracting the years and sorting them
years = [int(a.text) for a in pub_lv1_parse]
sorted_years = sorted(years)

# Output sorted years
print(sorted_years)
