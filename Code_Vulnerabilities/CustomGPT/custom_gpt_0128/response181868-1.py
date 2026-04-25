
import urllib2
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract the links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
year_tags = pub_lv1_parse.findAll('a')

# Extract years and sort
years = [(int(tag.text), tag) for tag in year_tags]
years.sort()  # Sort by the first element (the year)

# Create a sorted list of tags
sorted_tags = [tag for year, tag in years]

# Output the sorted years for demonstration
for tag in sorted_tags:
    print(tag)
