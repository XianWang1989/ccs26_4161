
import urllib2
from bs4 import BeautifulSoup

# Fetch the content
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1)

# Extract the relevant tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags based on the year extracted from the href attribute
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag['href'].split('/')[-1]))

# Print the sorted output
sorted_years = [tag.text for tag in sorted_tags]
print(sorted_years)
