
import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')  # Adjust the tag based on the HTML structure
    for article in articles:
        title = article.find('h2').text  # Change according to the actual HTML structure
        link = article.find('a')['href']  # Adjust if necessary
        print(f"Title: {title}\nLink: {link}\n")

# Example website URL to scrape
url = "https://example.com/articles"  # Replace with the articles page URL
scrape_articles(url)
