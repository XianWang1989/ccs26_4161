
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    next_url = feed_url

    while next_url:
        response = requests.get(next_url)
        feed = feedparser.parse(response.content)

        articles.extend(feed.entries)

        # Check if there's a 'next' link for pagination
        next_url = None
        for link in feed.links:
            if link.rel == 'next':
                next_url = link.href
                break

    return articles

if __name__ == "__main__":
    rss_feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
    all_articles = fetch_all_articles(rss_feed_url)

    for article in all_articles:
        print(article.title, article.link)
