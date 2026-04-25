
import urllib.request
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and extract the links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags by the year extracted from the href attribute
sorted_pub_lv1_parse = sorted(pub_lv1_parse, key=lambda tag: int(tag['href'].split('/')[-1]))

# Print the sorted tag texts
sorted_years = [tag.text for tag in sorted_pub_lv1_parse]
print(sorted_years)
