
import urllib2
from bs4 import BeautifulSoup

# Fetch the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract the links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
years = pub_lv1_parse.findAll('a')

# Sort the years
sorted_years = sorted(years, key=lambda x: int(x.text))

# Print sorted results
for year in sorted_years:
    print(year)
