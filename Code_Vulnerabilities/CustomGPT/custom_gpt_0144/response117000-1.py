import feedparser

def fetch_all_entries(feed_url):
    all_entries = []
    next_url = feed_url

    while next_url:
        feed = feedparser.parse(next_url)
        all_entries.extend(feed.entries)

        # Check if there's a link to the next page
        next_url = None
        for link in feed.feed.get('links', []):
            if link.rel == 'next':
                next_url = link.href
                break

    return all_entries

# Example usage
rss_url = 'https://example.com/rss'
entries = fetch_all_entries(rss_url)

for entry in entries:
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}\n")
