
import urllib2
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage and parse it
request = urllib2.Request("http://www.dummyurl.com")
pub_lv1 = urllib2.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1)

# Step 2: Find the specific table and extract the 'a' tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Step 3: Extract years and sort them
# Create a list of tuples (year, tag)
year_tag_list = [(int(tag.string), tag) for tag in pub_lv1_parse]

# Step 4: Sort the list by year
sorted_year_tag_list = sorted(year_tag_list, key=lambda x: x[0])

# Step 5: Optionally, extract only the sorted tags or print the results
sorted_tags = [tag for year, tag in sorted_year_tag_list]

# Print sorted years for verification
for tag in sorted_tags:
    print(tag)  # This prints the sorted <a> tags
