
import urllib.request  # Change to urllib.request for Python 3
from bs4 import BeautifulSoup

# Request the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, "html.parser")

# Find the relevant table and extract <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = sorted([int(link.get_text()) for link in links])

# Display sorted years
print(years)
