
import urllib2
from bs4 import BeautifulSoup

# Sample code to extract links as per your original script
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1)
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sorting the BeautifulSoup tags based on the year
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Displaying the sorted tags
sorted_urls = [tag['href'] for tag in sorted_tags]
print(sorted_urls)
