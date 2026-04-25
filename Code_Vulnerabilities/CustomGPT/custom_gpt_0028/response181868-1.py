
import urllib.request  # Update import for urllib
from bs4 import BeautifulSoup

# Request to the URL
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the specific table and extract links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the links based on the year in the href attribute
sorted_links = sorted(pub_lv1_parse, key=lambda tag: int(tag['href'].split('/')[-1]))

# Print sorted links
for link in sorted_links:
    print(link)
