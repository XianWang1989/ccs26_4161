
import urllib2
from bs4 import BeautifulSoup

# Fetch the URL and parse the content
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(tag.text) for tag in pub_lv1_parse]
years.sort()

# Output sorted years
sorted_tags = [tag for year in years for tag in pub_lv1_parse if int(tag.text) == year]
print(sorted_tags)
