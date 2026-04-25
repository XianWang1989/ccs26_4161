
import urllib2
from bs4 import BeautifulSoup

# Replace with your actual URL
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extracting the years as strings from the BeautifulSoup tags and sorting them
years = [int(tag.get_text()) for tag in pub_lv1_parse]  # Extract year and convert to int
years.sort()  # Sort the years in ascending order

# Creating the sorted BeautifulSoup tags
sorted_tags = [f'<a href="/content/by/year/{year}">{year}</a>' for year in years]

# Print sorted tags
for tag in sorted_tags:
    print(tag)
