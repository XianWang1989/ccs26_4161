
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}}
        ]
    }
}

titles_and_urls = []

for item in obj_1[u'd'][u'results']:
    title = item[u'Title']
    url = item[u'data'][u'Url']
    titles_and_urls.append((title, url))

# Print the extracted titles and URLs
for title, url in titles_and_urls:
    print(f'Title: {title}, URL: {url}')
