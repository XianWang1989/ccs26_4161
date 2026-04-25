
import urllib2
from bs4 import BeautifulSoup

# Sample request to get the webpage content
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and all the 'a' tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
years_tags = pub_lv1_parse.findAll('a')

# Sort the tags based on the year extracted as integer from the text
sorted_years_tags = sorted(years_tags, key=lambda tag: int(tag.text))

# Print the sorted output
for tag in sorted_years_tags:
    print(tag)
