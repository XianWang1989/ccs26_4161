
import urllib2
from bs4 import BeautifulSoup

# Make request to the webpage
request = urllib2.Request("http://www.dummyurl.com")  # Replace with the actual URL
pub_lv1 = urllib2.urlopen(request)

# Parse the response with BeautifulSoup
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the BeautifulSoup tags based on the year extracted from the href attribute
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag['href'].split('/')[-1]))

# Output the sorted result
sorted_urls = [tag['href'] for tag in sorted_tags]
print(sorted_urls)
