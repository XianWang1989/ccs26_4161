
import urllib2
from bs4 import BeautifulSoup

# Example URL
url = "http://www.dummyurl.com"

# Fetch the page content
request = urllib2.Request(url)
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Parse the <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
year_links = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [(int(link.text), link) for link in year_links]  # Create a tuple of (year, link)
sorted_years = sorted(years)  # Sort the tuples by year

# Reconstruct the sorted order of <a> tags
sorted_links = [link for year, link in sorted_years]

# Output the sorted <a> tags
for link in sorted_links:
    print(link)
