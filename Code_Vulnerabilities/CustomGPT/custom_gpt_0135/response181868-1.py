
import urllib.request  # Use request instead of urllib2
from bs4 import BeautifulSoup

# Fetch content from the URL
url = "http://www.dummyurl.com"
request = urllib.request.Request(url)
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract the anchors
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(tag.get_text()) for tag in pub_lv1_parse]  # Extract year as integers
sorted_years = sorted(years)  # Sort the years

# Create sorted list of BeautifulSoup tags based on the sorted years
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.get_text()))

# Display sorted URLs
for tag in sorted_tags:
    print(tag)  # This will print each <a> tag in sorted order
