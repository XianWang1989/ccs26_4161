
import urllib.request  # Update to `urllib.request` for Python 3
from bs4 import BeautifulSoup

# Fetch the web page
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract all <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
year_links = pub_lv1_parse.findAll('a')

# Sort the years extracted from the <a> tags
sorted_years = sorted(year_links, key=lambda x: int(x.text))

# Print sorted URLs
for tag in sorted_years:
    print(tag['href'], tag.text)
