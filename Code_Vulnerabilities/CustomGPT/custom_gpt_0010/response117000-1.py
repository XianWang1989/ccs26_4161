
import feedparser

# Replace with your RSS feed URL
rss_url = 'http://example.com/rss'

def fetch_articles(rss_url):
    feed = feedparser.parse(rss_url)
    articles = []

    # Loop through entries in the feed
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    # Check for more entries if pagination is supported
    if 'next' in feed:
        next_url = feed['next']
        articles.extend(fetch_articles(next_url))

    return articles

all_articles = fetch_articles(rss_url)
for article in all_articles:
    print(f"Title: {article['title']}\nLink: {article['link']}\nPublished: {article['published']}\n")
