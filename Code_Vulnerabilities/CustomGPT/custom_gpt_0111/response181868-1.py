
import urllib2
from bs4 import BeautifulSoup

# Request the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)

# Parse the HTML
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract years and sort
years = sorted(pub_lv1_parse, key=lambda x: int(x.text))

# Display the sorted output
for year in years:
    print(year)
