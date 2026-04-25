
from bs4 import BeautifulSoup
import urllib.request  # Use urllib.request for Python 3

# Sample HTML (replace with your fetched HTML)
html = """
<body>
    <table class="proxy-archive-content-year-list">
        <tr><td><a href="/content/by/year/2011">2011</a></td></tr>
        <tr><td><a href="/content/by/year/2012">2012</a></td></tr>
        <tr><td><a href="/content/by/year/2013">2013</a></td></tr>
        <tr><td><a href="/content/by/year/2000">2000</a></td></tr>
        <tr><td><a href="/content/by/year/2001">2001</a></td></tr>
        <tr><td><a href="/content/by/year/2002">2002</a></td></tr>
        <tr><td><a href="/content/by/year/2003">2003</a></td></tr>
        <tr><td><a href="/content/by/year/2004">2004</a></td></tr>
        <tr><td><a href="/content/by/year/2005">2005</a></td></tr>
    </table>
</body>
"""

# Parse the HTML
pub_lv1_parse = BeautifulSoup(html, 'html.parser')
pub_lv1_parse = pub_lv1_parse.body.find('table', attrs={"class": "proxy-archive-content-year-list"})
pub_lv1_parse = pub_lv1_parse.findAll('a')

# Sort using the year extracted from the tag text
sorted_pub_lv1_parse = sorted(pub_lv1_parse, key=lambda tag: int(tag.text))

# Print sorted output
for tag in sorted_pub_lv1_parse:
    print(tag)
