
import feedparser

def fetch_all_articles(feed_url):
    articles = []
    while feed_url:
        # Parse the feed
        feed = feedparser.parse(feed_url)

        # Add the articles to our list
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published if 'published' in entry else 'No date'
            })

        # Look for a link to the next page (if applicable)
        feed_url = next((link.href for link in feed.links if link.rel == 'next'), None)

    return articles

# Example usage:
rss_feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_feed_url)

for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}\n")
