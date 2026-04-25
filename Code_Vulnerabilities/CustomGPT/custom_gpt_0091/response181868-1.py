
import urllib2
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, "html.parser")

# Find the relevant table and extract anchor tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
years_tags = pub_lv1_parse.findAll('a')

# Extract the year as strings and sort them
years = [int(tag.text) for tag in years_tags]
years.sort()

# Construct sorted output using the original tags
sorted_years_tags = sorted(years_tags, key=lambda tag: int(tag.text))

# Print sorted years
sorted_years = [tag.text for tag in sorted_years_tags]
print(sorted_years)
