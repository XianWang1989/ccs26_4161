
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')  # Specify the parser

# Find the table and all anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and their corresponding tags into a list
year_tags = [(int(tag.get_text()), tag) for tag in pub_lv1_parse]

# Sort the list by year
sorted_year_tags = sorted(year_tags, key=lambda x: x[0])

# Extract the sorted tags
sorted_tags = [tag for year, tag in sorted_year_tags]

# Output the sorted tags
for tag in sorted_tags:
    print(tag)
