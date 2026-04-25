
from bs4 import BeautifulSoup
import urllib.request

# Fetch the webpage
request = urllib.request.Request("http://www.dummyurl.com")
pub_lv1 = urllib.request.urlopen(request)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the table and extract anchor elements
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
years_links = pub_lv1_parse.findAll('a')

# Extract years and sort them
years = [int(link.text) for link in years_links]
years.sort()

# Print sorted years
sorted_years = [f'<a href="{link["href"]}">{link.text}</a>' for link in years_links if int(link.text) in years]

print(sorted_years)
