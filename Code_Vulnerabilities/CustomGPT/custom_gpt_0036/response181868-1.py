
import urllib2
from bs4 import BeautifulSoup

# Request URL and read data
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Extract the table and find all <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags based on the text content (the year)
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Print the sorted output
for tag in sorted_tags:
    print(tag)
