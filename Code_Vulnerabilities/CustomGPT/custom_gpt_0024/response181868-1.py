
import urllib2
from bs4 import BeautifulSoup

# Fetching the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Extracting the desired table and links
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_links = pub_lv1_parse.findAll('a')

# Extracting years from the tags and sorting them
years = [int(link.text) for link in pub_lv1_links]
years.sort()

# Displaying the sorted years
sorted_links = [link for year in years for link in pub_lv1_links if link.text == str(year)]
sorted_links_output = [link for link in sorted_links]

print(sorted_links_output)
