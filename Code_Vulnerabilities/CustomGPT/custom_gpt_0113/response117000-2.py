
import requests
from bs4 import BeautifulSoup

# URL of the page with older articles
url = 'https://example.com/articles'

# Send a GET request
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find article links (the selector will depend on the website structure)
for article in soup.find_all('a', class_='article-link'):
    title = article.get_text()
    link = article['href']
    print(f'Title: {title}\nLink: {link}\n')
