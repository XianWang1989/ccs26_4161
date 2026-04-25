
from bs4 import BeautifulSoup
import urllib2

# Request the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)

# Parse the HTML
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = sorted([int(tag.text) for tag in pub_lv1_parse])

# Create new sorted list of tags
sorted_tags = [f'<a href="/content/by/year/{year}">{year}</a>' for year in years]

# Output the sorted tags
print(sorted_tags)
