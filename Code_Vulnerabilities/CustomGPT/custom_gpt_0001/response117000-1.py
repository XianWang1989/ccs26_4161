
import feedparser

# Define the RSS feed URL
rss_url = 'https://your-rss-feed-url.com/rss'  # Replace with your RSS feed URL

def fetch_all_articles(url):
    all_articles = []
    feed = feedparser.parse(url)

    # Store the current feed articles
    all_articles.extend(feed.entries)

    # Check if there is a next page or older articles are accessible
    next_link = feed.get('feed', {}).get('link')  # This link should lead to the next page of articles

    # Loop to fetch additional pages if available
    while next_link:
        feed = feedparser.parse(next_link)
        all_articles.extend(feed.entries)
        next_link = feed.get('feed', {}).get('link')  # Update to the next page link

    return all_articles

# Fetching all articles
articles = fetch_all_articles(rss_url)

# Print article titles
for article in articles:
    print(article.title)
