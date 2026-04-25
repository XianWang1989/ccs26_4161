
from bs4 import BeautifulSoup
import urllib.request  # Use urllib.request in Python 3

# Assuming you have the necessary imports and have fetched the HTML

request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the years and sort them
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Display sorted output
for year_tag in sorted_years:
    print(year_tag)
