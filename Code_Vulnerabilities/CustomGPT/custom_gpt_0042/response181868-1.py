
import urllib2
from bs4 import BeautifulSoup

# Fetch the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Extract years from links and sort
years = [int(link.text) for link in links]  # Convert to integers for proper sorting
years.sort()  # Sort the list of years

# Print the sorted years
print(years)
