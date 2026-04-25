
import urllib.request  # Use 'import urllib2' for Python 2
from bs4 import BeautifulSoup

# Replace with your URL
request = urllib.request.Request("http://www.dummyurl.com")  # Adjust for Python 2 if needed
pub_lv1 = urllib.request.urlopen(request)  # Adjust for Python 2 if needed
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the tags by year
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.get_text()))

# Output the sorted URLs
sorted_urls = [tag['href'] for tag in sorted_tags]
print(sorted_urls)
