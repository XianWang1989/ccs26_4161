
from urllib import request
from bs4 import BeautifulSoup

# Sample URL (replace with your actual URL)
url = "http://www.dummyurl.com"
pub_lv1 = request.urlopen(url)
pub_lv1_parse = BeautifulSoup(pub_lv1, 'html.parser')

# Find the desired table and extract all <a> tags
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
year_tags = pub_lv1_parse.findAll('a')

# Extract years from tags, convert them to integers, and sort them
sorted_years = sorted(int(tag.get_text()) for tag in year_tags)

# If you want to output the sorted tags:
sorted_year_tags = [f'<a href="/content/by/year/{year}">{year}</a>' for year in sorted_years]

print(sorted_year_tags)  # This will print the sorted list of <a> tags
