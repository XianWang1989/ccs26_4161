
import urllib2
from bs4 import BeautifulSoup

# Make the request and parse the response
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the years and sort them
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.get_text()))

# Print sorted URLs with years
sorted_urls = [(tag.get_text(), tag['href']) for tag in sorted_tags]
print(sorted_urls)
