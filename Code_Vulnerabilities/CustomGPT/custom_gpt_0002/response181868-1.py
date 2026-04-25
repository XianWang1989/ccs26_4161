
import urllib2
from bs4 import BeautifulSoup

# Fetching the content
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1)

# Finding the specific table and extracting links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sorting the tags based on the year in the text
sorted_years = sorted(pub_lv1_parse, key=lambda x: int(x.text))

# Output the sorted years
for year in sorted_years:
    print(year)
