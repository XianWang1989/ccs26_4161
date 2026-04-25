
import urllib2
from bs4 import BeautifulSoup

# Make a request to the URL
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)

# Parse the content with BeautifulSoup
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class":"proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Extract the years from the tags and sort them
years = [int(tag.text) for tag in pub_lv1_parse]  # Extracting the year values as integers
sorted_years = sorted(years)  # Sorting the list of years

# Display sorted output
print(sorted_years)

# If you want to get back the corresponding tags after sorting, you can do as follows:
sorted_tags = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Output the sorted tags if needed
print(sorted_tags)
