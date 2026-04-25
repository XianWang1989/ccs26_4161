
import urllib2
from bs4 import BeautifulSoup

# Request the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(tag.text) for tag in pub_lv1_parse]  # Extract years as integers
sorted_years = sorted(years)  # Sort the years

# Print sorted years
print(sorted_years)

# If you want the sorted tags:
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))  # Sort tags based on year text
for tag in sorted_tags:
    print(tag)
