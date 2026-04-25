
from urllib import request
from bs4 import BeautifulSoup

# Fetching the content
url = "http://www.dummyurl.com"
response = request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')

# Extracting the table links
pub_lv1_parse = soup.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Extracting years and sorting
years = [int(link.text) for link in links]
years.sort()

# Printing sorted years
print(years)
