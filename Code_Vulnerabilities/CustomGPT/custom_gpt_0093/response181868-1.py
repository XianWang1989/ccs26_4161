
import urllib.request  # urllib2 is for Python 2; use urllib.request for Python 3
from bs4 import BeautifulSoup

# Example URL (replace with your actual URL)
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and all anchor tags within it
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(tag.text) for tag in pub_lv1_parse]  # Convert text to int
years.sort()  # Sort the list of years

# Output sorted years as desired tags
sorted_tags = [f'<a href="/content/by/year/{year}">{year}</a>' for year in years]

# Print the sorted tags
for tag in sorted_tags:
    print(tag)
