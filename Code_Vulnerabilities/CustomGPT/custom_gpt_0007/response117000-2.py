
import requests
from bs4 import BeautifulSoup

def scrape_all_articles(page_url):
    all_articles = []
    while page_url:
        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Parse articles from the HTML (you'll need to adjust the selectors based on the site's structure)
        articles = soup.find_all('article')
        for article in articles:
            all_articles.append({
                'title': article.find('h2').text,
                'link': article.find('a')['href'],
                'published': article.find('time')['datetime'],
                'summary': article.find('p').text
            })

        # Logic to find the next page URL
        next_page = soup.find('a', class_='next')  # Example selector
        page_url = next_page['href'] if next_page else None

    return all_articles

# Example website URL
website_url = 'http://example.com/articles'  # Replace with a valid URL
articles = scrape_all_articles(website_url)

# Print the articles
for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print(f"Summary: {article['summary']}\n")
