
def fetch_all_articles_with_pagination(feed_url):
    page = 1
    all_articles = []

    while True:
        paged_url = f"{feed_url}?page={page}"
        feed = feedparser.parse(paged_url)

        if not feed.entries:
            break  # Exit if no more articles

        for entry in feed.entries:
            all_articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published
            })

        page += 1  # Go to the next page

    return all_articles
