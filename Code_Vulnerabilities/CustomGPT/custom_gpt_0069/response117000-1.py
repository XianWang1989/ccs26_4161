
import feedparser
import requests

def fetch_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []

    # Collecting articles from the first page
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    # Check for links to older articles (this varies by feed)
    # Example: if feed has a 'next' link, follow it
    if 'next' in feed:
        next_page = feed.next
        while next_page:
            feed = feedparser.parse(next_page)
            for entry in feed.entries:
                articles.append({
                    'title': entry.title,
                    'link': entry.link,
                    'published': entry.published
                })
            # Update the next_page if it exists
            next_page = feed.get('next', None)

    return articles

# Example usage
rss_url = 'https://example.com/rss'
all_articles = fetch_articles(rss_url)

for article in all_articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
