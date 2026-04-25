
import urllib2
from bs4 import BeautifulSoup

# Fetch the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and all anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_tags = pub_lv1_parse.findAll('a')

# Create a list of tuples (year, tag)
year_tag_pairs = [(int(tag.text), tag) for tag in pub_lv1_tags]

# Sort the list by year
year_tag_pairs.sort(key=lambda x: x[0])

# If you need just the sorted tags
sorted_tags = [pair[1] for pair in year_tag_pairs]

# Print sorted years
for tag in sorted_tags:
    print(tag)
