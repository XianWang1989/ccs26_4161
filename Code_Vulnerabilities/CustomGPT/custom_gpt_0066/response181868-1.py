
import urllib.request  # Use urllib.request instead of urllib2 in Python 3
from bs4 import BeautifulSoup

# Fetch and parse the content
url = "http://www.dummyurl.com"
request = urllib.request.Request(url)
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract the links
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Sort the links by the year text
sorted_links = sorted(links, key=lambda link: int(link.text))

# Print sorted URLs
sorted_urls = [link['href'] for link in sorted_links]
print(sorted_urls)
