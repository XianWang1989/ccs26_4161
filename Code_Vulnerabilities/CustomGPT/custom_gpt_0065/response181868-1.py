
import urllib.request  # Use urllib.request for Python 3
from bs4 import BeautifulSoup

# Fetch the webpage
request = urllib.request.Request("http://www.dummyurl.com")
with urllib.request.urlopen(request) as response:
    pub_lv1 = response.read()

# Parse the page
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')
table = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = table.findAll('a')

# Extracting years and sorting
years = sorted(int(link.text) for link in links)

# Creating sorted links based on the sorted years
sorted_links = [next(link for link in links if link.text == str(year)) for year in years]

# Output sorted links
for link in sorted_links:
    print(link)
