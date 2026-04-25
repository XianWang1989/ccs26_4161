
from bs4 import BeautifulSoup
import urllib2

# Your initial request and parsing
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the years and sort them
years = [int(tag.text) for tag in pub_lv1_parse]
years.sort()

# Use the sorted years to create a sorted list of URLs
sorted_links = [tag for year in years for tag in pub_lv1_parse if tag.text == str(year)]

# Output the sorted links
for link in sorted_links:
    print(link)
