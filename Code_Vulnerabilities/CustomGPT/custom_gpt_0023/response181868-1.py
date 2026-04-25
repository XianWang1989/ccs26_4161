
import urllib2
from bs4 import BeautifulSoup

# Fetch the page
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the specific table and all <a> tags within it
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(link.text) for link in links]   # Convert text to integers
years.sort()                                   # Sort the years

# Create sorted <a> tags
sorted_links = [f'<a href="{link["href"]}">{year}</a>' for year, link in sorted(zip(years, links), key=lambda x: x[0])]

# Output the sorted links
print(sorted_links)
