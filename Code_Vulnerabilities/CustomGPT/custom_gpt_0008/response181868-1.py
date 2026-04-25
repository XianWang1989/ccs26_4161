
import urllib2
from bs4 import BeautifulSoup

# Fetch the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract links
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Extract the years and sort them
years = [int(link.text) for link in links]
years.sort()

# For sorted output, find the tags corresponding to the sorted years
sorted_links = sorted(links, key=lambda link: int(link.text))

# Output the sorted links
for link in sorted_links:
    print(link)
