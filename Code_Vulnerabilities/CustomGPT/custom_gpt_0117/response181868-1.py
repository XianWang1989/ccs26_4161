
import urllib.request  # Use urllib.request in Python 3
from bs4 import BeautifulSoup

# URL request and parsing
url = "http://www.dummyurl.com"
request = urllib.request.Request(url)
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Extract the links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Sort the links based on their text (the year)
sorted_links = sorted(links, key=lambda x: int(x.text))

# Display sorted URLs
sorted_urls = [link['href'] for link in sorted_links]
print(sorted_urls)
