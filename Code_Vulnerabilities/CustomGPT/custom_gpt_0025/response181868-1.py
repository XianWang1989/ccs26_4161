
import urllib2
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)

# Parse the webpage
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Print sorted URLs
sorted_urls = [tag['href'] for tag in sorted_years]
print(sorted_urls)
