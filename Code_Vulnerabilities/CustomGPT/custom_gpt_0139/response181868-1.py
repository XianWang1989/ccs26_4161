
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Request the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table containing the year links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the years and sort them
years = [int(a.get_text()) for a in pub_lv1_parse]  # Extract text and convert to int
years.sort()  # Sort the list of years

# Print the sorted years
print(years)

# If you want to keep the original BeautifulSoup tags sorted as well, you can do it like this:
sorted_tags = sorted(pub_lv1_parse, key=lambda a: int(a.get_text()))

# Display the sorted tags
for tag in sorted_tags:
    print(tag)
