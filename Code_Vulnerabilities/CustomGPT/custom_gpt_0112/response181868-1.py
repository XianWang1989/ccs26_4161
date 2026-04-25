
import urllib2
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table
table = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
year_tags = table.findAll('a')

# Extract text and sort
years = sorted([int(tag.text) for tag in year_tags])

# Print the sorted years
print(years)
