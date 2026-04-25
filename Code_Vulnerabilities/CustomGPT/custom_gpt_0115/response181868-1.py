
import urllib.request  # Use this for Python 3
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the relevant table and all anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
url_tags = pub_lv1_parse.findAll('a')

# Sort the tags based on the year extracted from their text
sorted_url_tags = sorted(url_tags, key=lambda tag: int(tag.text))

# Print the sorted URLs
sorted_urls = [tag['href'] for tag in sorted_url_tags]
print(sorted_urls)
