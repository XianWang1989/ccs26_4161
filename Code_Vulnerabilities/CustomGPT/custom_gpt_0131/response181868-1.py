
from bs4 import BeautifulSoup
import urllib.request  # use this for Python 3

# Example to extract and sort BeautifulSoup tags
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract all anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the anchor tags based on the year extracted from the href attribute
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag['href'].split('/')[-1]))

# Output the sorted result
for tag in sorted_tags:
    print(tag)  # This will display each tag sorted by year
