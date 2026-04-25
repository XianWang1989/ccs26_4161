
from bs4 import BeautifulSoup
import urllib.request  # For Python 3. Use urllib2 for Python 2.

# Fetch and parse the HTML
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort
years = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Display sorted output
for year in years:
    print(year)
