
import urllib.request
from bs4 import BeautifulSoup

# Fetch and parse the HTML
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the year and sort the tags
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Output the sorted URLs
sorted_urls = [tag['href'] for tag in sorted_tags]
print(sorted_urls)
