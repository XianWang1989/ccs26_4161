
import urllib2
from bs4 import BeautifulSoup

# Fetch the URL
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract the <a> tags
proxy_list = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
years_tags = proxy_list.findAll('a')

# Sort the tags based on the year extracted from the text
sorted_years_tags = sorted(years_tags, key=lambda tag: int(tag.text))

# Print the sorted URLs
for tag in sorted_years_tags:
    print(f"{tag['href']} - {tag.text}")
