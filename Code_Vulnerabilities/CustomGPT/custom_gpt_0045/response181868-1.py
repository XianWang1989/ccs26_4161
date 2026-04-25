
import urllib2
from bs4 import BeautifulSoup

# Step 1: Get the page content
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Step 2: Find the desired table and extract all <a> tags
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
year_links = table.findAll('a')

# Step 3: Extract the year and sort the list
# Using a key function to extract the year from the tag
sorted_year_links = sorted(year_links, key=lambda tag: int(tag.text))

# Print the sorted list
for link in sorted_year_links:
    print(link)
