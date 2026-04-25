
def fetch_all_articles(base_url):
    articles = []
    page = 1

    while True:
        # Alter the URL based on pagination (if applicable)
        rss_feed_url = f'{base_url}?page={page}'
        feed = feedparser.parse(rss_feed_url)

        # Break if we have no more articles
        if not feed.entries:
            break

        # Collect articles
        articles.extend(feed.entries)
        page += 1  # Go to next page

    return articles

# Example usage with a hypothetical paginated feed
all_articles = fetch_all_articles('https://example.com/rss')

for entry in all_articles:
    print(f'Title: {entry.title}')
    print(f'Link: {entry.link}')
    print(f'Published: {entry.published}\n')
