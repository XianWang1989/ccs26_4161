
def read_full_rss_feed(url):
    all_articles = []
    next_url = url

    while next_url:
        feed = feedparser.parse(next_url)
        all_articles.extend(feed.entries)

        # Check for pagination (this might vary based on the feed)
        next_url = None
        if 'next' in feed:
            next_url = feed.next  # Replace 'next' with the actual key if different

    return all_articles
