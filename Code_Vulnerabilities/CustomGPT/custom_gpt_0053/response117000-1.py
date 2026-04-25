
import feedparser

def fetch_feed(url):
    feed = feedparser.parse(url)
    articles = feed.entries
    return articles

def main():
    url = 'https://example.com/rss'  # Replace with your RSS feed URL
    all_articles = []

    # Fetch the first set of articles
    articles = fetch_feed(url)
    all_articles.extend(articles)

    # Check if there’s a next page (this depends on the feed's structure)
    while getattr(feedparser.parse(url), 'links', []):
        for link in feedparser.parse(url).links:
            if link.rel == 'next':
                url = link.href
                articles = fetch_feed(url)
                all_articles.extend(articles)
                break
        else:
            break  # No more pages

    # Print the titles of all articles
    for article in all_articles:
        print(article.title)

if __name__ == "__main__":
    main()
