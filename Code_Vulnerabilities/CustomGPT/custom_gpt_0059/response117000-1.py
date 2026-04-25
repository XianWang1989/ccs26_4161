
import feedparser
import requests

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    return feed.entries

def fetch_all_articles(feed_url):
    all_articles = []
    page_number = 1  # Initialize pagination variable (if applicable)

    while True:
        # Modify this if your RSS feed supports paging differently
        url = f"{feed_url}?page={page_number}"  
        articles = fetch_rss_feed(url)

        if not articles:  # If no more articles are returned, break the loop
            break

        all_articles.extend(articles)
        page_number += 1  # Increment to the next page

    return all_articles

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_url)

for article in all_articles:
    print(article.title, article.link)
