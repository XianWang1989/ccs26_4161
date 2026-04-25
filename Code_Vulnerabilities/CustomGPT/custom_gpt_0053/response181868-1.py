
import urllib2
from bs4 import BeautifulSoup

# Request the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1)

# Find the specific table and all <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
year_tags = pub_lv1_parse.findAll('a')

# Extract the years as integers
years = [int(tag.text) for tag in year_tags]

# Sort the years
years.sort()

# Print sorted years
print(years)
