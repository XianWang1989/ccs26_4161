
import urllib2
from bs4 import BeautifulSoup

# Fetch and parse the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract all <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the text (year) and sort the list
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# If you wish to output the sorted URLs
sorted_urls = [tag['href'] for tag in sorted_years]
print(sorted_urls)
