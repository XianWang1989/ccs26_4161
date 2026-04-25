
import urllib2
from bs4 import BeautifulSoup

# Make the request and parse the content
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and all anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the years and sort them
# Create a list of years by converting the text to integers
years = [int(tag.text) for tag in pub_lv1_parse]

# Sort the years list
years.sort()

# Output the sorted years
print(years)
