
def read_all_articles(feed_url):
    articles = []
    page = 1

    while True:
        current_feed_url = f"{feed_url}?page={page}"  # Adjust the parameter as necessary
        feed = feedparser.parse(current_feed_url)

        if not feed.entries:
            break  # Break if no more entries

        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'summary': entry.summary
            })

        page += 1

    return articles

rss_url = 'https://your-rss-feed-url-here.com/feed'
all_articles = read_all_articles(rss_url)

for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print(f"Summary: {article['summary']}\n")
