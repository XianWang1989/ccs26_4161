
import urllib2
from bs4 import BeautifulSoup

# Fetching the URL
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Finding the relevant table and all anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
year_tags = pub_lv1_parse.findAll('a')

# Extracting years and sorting them
years = sorted(int(tag.get_text()) for tag in year_tags)

# Displaying sorted years
sorted_tags = [tag for year in years for tag in year_tags if tag.get_text() == str(year)]
print(sorted_tags)
