
from bs4 import BeautifulSoup
import urllib.request  # Use urllib.request for Python 3

# Sample output simulating the BeautifulSoup tag extraction
html_content = '''
<body>
    <table class="proxy-archive-content-year-list">
        <a href="/content/by/year/2011">2011</a>
        <a href="/content/by/year/2012">2012</a>
        <a href="/content/by/year/2013">2013</a>
        <a href="/content/by/year/2000">2000</a>
        <a href="/content/by/year/2001">2001</a>
        <a href="/content/by/year/2002">2002</a>
        <a href="/content/by/year/2003">2003</a>
        <a href="/content/by/year/2004">2004</a>
        <a href="/content/by/year/2005">2005</a>
    </table>
</body>
'''

# Simulating the BeautifulSoup parsing
pub_lv1_parse = BeautifulSoup(html_content, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
links = pub_lv1_parse.findAll('a')

# Sorting logic
links_sorted = sorted(links, key=lambda x: int(x.text))

# Output result
for link in links_sorted:
    print(link)
