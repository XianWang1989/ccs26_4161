
import urllib2
from bs4 import BeautifulSoup

# Fetch and parse the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract the URLs
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags by their text content (the year)
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Print the sorted URLs
sorted_urls = [tag['href'] for tag in sorted_years]
print(sorted_urls)
