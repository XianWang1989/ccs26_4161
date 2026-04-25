
import feedparser

def fetch_all_articles(feed_url):
    articles = []
    url = feed_url

    while url:
        # Parse the feed
        feed = feedparser.parse(url)

        # Add articles to the list
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published
            })

        # Check for the next page (if available)
        # This can vary based on the feed. Here, we assume there's a "next" link
        try:
            url = feed.feed.link  # You may need to adjust this if the next link structure is different
        except AttributeError:
            break  # No more pages available

    return articles

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_url)

# Print the fetched articles
for article in all_articles:
    print(f'Title: {article["title"]}, Link: {article["link"]}, Published: {article["published"]}')
