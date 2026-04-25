
import urllib.request
from bs4 import BeautifulSoup

# Fetch the page
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Extract the links
links = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"}).findAll('a')

# Sort the links based on the year
sorted_links = sorted(links, key=lambda x: int(x.text))

# Print the sorted output
for link in sorted_links:
    print(link)
