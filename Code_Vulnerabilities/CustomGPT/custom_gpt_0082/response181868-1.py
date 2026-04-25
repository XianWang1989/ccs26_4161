
import urllib.request  # Updated import for Python 3
from bs4 import BeautifulSoup

# Your existing code
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [(int(tag.text), tag) for tag in pub_lv1_parse]  # Create a list of tuples (year, tag)
years.sort()  # Sort by the first element of the tuple (the year)

# Extract the sorted tags
sorted_tags = [tag for year, tag in years]

# Output the sorted tags
for tag in sorted_tags:
    print(tag)
