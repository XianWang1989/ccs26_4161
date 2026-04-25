
import feedparser

def read_all_articles(url):
    feed = feedparser.parse(url)

    while True:
        for entry in feed.entries:
            print(f"Title: {entry.title}")
            print(f"Link: {entry.link}")
            print(f"Published: {entry.published}")
            print()

        # Check for a link to the next page
        next_page = None
        if 'next' in feed:
            next_page = feed.next
        elif hasattr(feed, 'feed') and 'link' in feed.feed:
            # Example if there's a pagination link in the feed
            next_page = feed.feed.link

        if not next_page:
            break

        feed = feedparser.parse(next_page)

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
read_all_articles(rss_url)
