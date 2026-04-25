
import urllib2
from bs4 import BeautifulSoup

# Make the request to the URL and parse the content
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, "html.parser")

# Find the specific table and extract the 'a' tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_tags = pub_lv1_parse.findAll('a')

# Extract the years and sort them
years = [int(tag.string) for tag in pub_lv1_tags]
years.sort()

# Now create a sorted list of tags based on the sorted years
sorted_tags = sorted(pub_lv1_tags, key=lambda tag: int(tag.string))

# Display the sorted tags
for tag in sorted_tags:
    print(tag)
