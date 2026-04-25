
import urllib2
from bs4 import BeautifulSoup

# Request the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1)

# Find the table and extract the 'a' tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags based on the year text
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# If you need the sorted URLs
sorted_urls = [tag['href'] for tag in sorted_tags]

# Print the sorted years and their URLs
for tag in sorted_tags:
    print(tag.text, tag['href'])
