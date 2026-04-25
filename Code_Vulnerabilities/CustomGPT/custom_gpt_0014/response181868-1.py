
import urllib.request  # Update urllib2 to urllib
from bs4 import BeautifulSoup

# Fetch and parse the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(tag.string) for tag in pub_lv1_parse]  # Convert strings to integers
sorted_years = sorted(years)  # Sort the years

# Create a new sorted list of tags based on years
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.string))

# Output sorted tags
sorted_output = [str(tag) for tag in sorted_tags]
print(sorted_output)
