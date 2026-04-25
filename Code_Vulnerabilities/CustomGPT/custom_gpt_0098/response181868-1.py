
import urllib.request
from bs4 import BeautifulSoup

# Fetch the page
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract all <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Extract the year from each <a> tag and store them as tuples (year, tag)
year_tags = [(int(link.text), link) for link in links]

# Sort the list by year
year_tags.sort(key=lambda x: x[0])

# Extract the sorted tags
sorted_links = [tag for year, tag in year_tags]

# Print the sorted links
for link in sorted_links:
    print(link)
