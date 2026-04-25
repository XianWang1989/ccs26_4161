
import urllib2
from bs4 import BeautifulSoup

# Example code to fetch and parse the HTML
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort the BeautifulSoup tags based on the year
sorted_years = sorted(pub_lv1_parse, key=lambda tag: int(tag['href'].split('/')[-1]))

# Print the sorted results
for tag in sorted_years:
    print(tag, tag['href'])
