
def read_paginated_rss_feed(base_url, total_pages):
    articles = []
    for page in range(1, total_pages + 1):
        url = f"{base_url}?page={page}"
        feed = feedparser.parse(url)
        articles.extend(feed.entries)

    # Print all articles
    for entry in articles:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print()

# Example RSS feed with pagination
rss_base_url = 'https://example.com/rss'
read_paginated_rss_feed(rss_base_url, 5)  # adjust total_pages as needed
