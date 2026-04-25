from bs4 import BeautifulSoup
import urllib.request  # Use urllib.request for Python 3

# Sample HTML (replace with actual request/response if needed)
html = """
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
"""

soup = BeautifulSoup(html, 'html.parser')
links = soup.find('table', class_="proxy-archive-content-year-list").find_all('a')

# Sort by the integer value of the text content
sorted_links = sorted(links, key=lambda x: int(x.text))

# Output sorted result
for link in sorted_links:
    print(link)
