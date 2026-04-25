
import urllib2
from bs4 import BeautifulSoup

# Fetch the content from the URL
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the specific table and extract the links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Extract years from the tags
years = [(int(link.text), link) for link in links]

# Sort the list by year
sorted_years = sorted(years)

# Extract sorted links
sorted_links = [link for year, link in sorted_years]

# Print the sorted output
for link in sorted_links:
    print(link)
