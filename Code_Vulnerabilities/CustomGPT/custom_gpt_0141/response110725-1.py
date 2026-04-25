
# Sample dictionary similar to obj_1 you've provided
obj_1 = {
    u'd': {
        u'results': [
            {
                u'Desc': u'This is a description...',
                u'Title': u'This is a title 1...',
                u'data': {u'Url': u'www.site1.com'}
            },
            {
                u'Desc': u'This is a description...',
                u'Title': u'This is a title 2...',
                u'data': {u'Url': u'www.site2.com'}
            }
        ]
    }
}

# Extracting Title and Url
titles_and_urls = []
for result in obj_1[u'd'][u'results']:
    title = result[u'Title']
    url = result[u'data'][u'Url']
    titles_and_urls.append((title, url))

# Printing the extracted titles and urls
for title, url in titles_and_urls:
    print(f'Title: {title}, URL: {url}')
