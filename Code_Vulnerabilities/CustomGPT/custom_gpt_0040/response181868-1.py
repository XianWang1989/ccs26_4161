
import urllib2
from bs4 import BeautifulSoup

# Fetching the HTML content
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Finding the relevant table and extracting links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Extracting years and sorting
# This creates a list of tuples (year, tag)
year_tag_pairs = [(int(link.text), link) for link in links]

# Sorting by year
sorted_year_tag_pairs = sorted(year_tag_pairs)

# Getting the sorted tags back
sorted_tags = [tag for year, tag in sorted_year_tag_pairs]

# Printing the sorted tags
for tag in sorted_tags:
    print(tag)
