
def read_paginated_rss_feed(base_url):
    articles = []
    page = 1

    while True:
        url = f"{base_url}?page={page}"  # Adjust based on the feed's pagination setup
        feed = feedparser.parse(url)

        if not feed.entries:
            break  # Exit if no more articles

        for entry in feed.entries:
            article = {
                'title': entry.title,
                'link': entry.link,
                'published': entry.published
            }
            articles.append(article)

        page += 1  # Move to the next page

    return articles
