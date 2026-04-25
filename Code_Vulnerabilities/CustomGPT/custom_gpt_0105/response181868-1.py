
import urllib2
from bs4 import BeautifulSoup

# Fetch and parse the URL
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract the 'a' tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
tags = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(tag.text) for tag in tags]  # Convert tag texts to integers
sorted_years = sorted(years)  # Sort the list of years

# Print sorted tags
sorted_tags = sorted(tags, key=lambda tag: int(tag.text))  # Sort tags based on year text

# Output sorted results
for tag in sorted_tags:
    print(tag)
