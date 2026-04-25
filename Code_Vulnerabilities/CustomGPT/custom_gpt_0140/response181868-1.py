
import urllib2
from bs4 import BeautifulSoup

# Fetching the content
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Extracting the relevant table
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sorting the tags based on the year in their text
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Output the sorted results
for year_tag in sorted_years:
    print(year_tag)
