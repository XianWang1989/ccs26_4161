
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)
    articles = []

    # Loop through all the entries in the RSS feed
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary
        })

    return articles

# Example RSS feed URL
rss_url = 'http://example.com/rss'  # Replace with a valid RSS feed URL
articles = read_rss_feed(rss_url)

# Print the articles
for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print(f"Summary: {article['summary']}\n")
