
import urllib2
from bs4 import BeautifulSoup

# Fetching the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Extracting the anchors from the specified table
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
years_tags = pub_lv1_parse.findAll('a')

# Extracting years and sorting them
years = sorted(int(tag.text) for tag in years_tags)

# Output sorted years
sorted_years_tags = [tag for year in years for tag in years_tags if year == int(tag.text)]
for tag in sorted_years_tags:
    print(tag)
