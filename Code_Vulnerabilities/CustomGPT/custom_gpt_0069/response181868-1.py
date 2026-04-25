
import urllib2
from bs4 import BeautifulSoup

# Fetch and parse the HTML
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the desired table and all <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
years_tags = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(tag.text) for tag in years_tags]  # Convert to integers
sorted_years = sorted(years)  # Sort the years

# Optional: Create sorted tag list if you need the <a> tags in sorted order
sorted_tags = sorted(years_tags, key=lambda tag: int(tag.text))

# Printing the sorted years
print(sorted_years)

# Printing the sorted <a> tags
for tag in sorted_tags:
    print(tag)
