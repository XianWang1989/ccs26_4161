
import urllib2
from bs4 import BeautifulSoup

# Fetch the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the specific table and extract all 'a' tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
year_tags = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(tag.get_text()) for tag in year_tags]
years.sort()

# Output sorted years
sorted_year_tags = [tag for year in years for tag in year_tags if int(tag.get_text()) == year]
print(sorted_year_tags)
