
import urllib.request  # Use urllib for Python 3
from bs4 import BeautifulSoup

# Make a request to the URL
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years from tags and sort them
years = [(int(tag.text), tag) for tag in pub_lv1_parse]  # Create a tuple of (year as int, tag)
sorted_years = sorted(years, key=lambda x: x[0])  # Sort by year

# Extract the sorted tags
sorted_tags = [tag[1] for tag in sorted_years]

# Output the sorted tags
for tag in sorted_tags:
    print(tag)
