
import urllib2
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and all the <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the year and sort
years = [(int(tag.text), tag) for tag in pub_lv1_parse]  # Create a list of tuples (year, tag)
years.sort()  # Sort by the first element of the tuple (year)

# Get the sorted tags back
sorted_tags = [tag for year, tag in years]

# Print the sorted tags
for tag in sorted_tags:
    print(tag)
