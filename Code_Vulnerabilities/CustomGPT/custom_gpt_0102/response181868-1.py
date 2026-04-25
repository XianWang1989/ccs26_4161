
import urllib2
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1)

# Find the specific table and extract the anchor tags
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Extract years from the tags and convert to integers for sorting
years = [int(link.text) for link in links]

# Sort the years
years.sort()

# Output the sorted years
sorted_links = [link for year in years for link in links if link.text == str(year)]
sorted_links

# If you want to print the sorted links
for link in sorted_links:
    print(link)
