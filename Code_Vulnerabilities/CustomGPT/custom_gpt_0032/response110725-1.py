
# Sample dictionary
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...',
             u'Title': u'This is another title...',
             u'data': {u'Url': u'www.another-site.com'}}
        ]
    }
}

# Extracting Title and URL values
titles_urls = []

for item in obj_1[u'd'][u'results']:
    title = item[u'Title']
    url = item[u'data'][u'Url']
    titles_urls.append((title, url))

# Displaying the extracted values
for title, url in titles_urls:
    print(f'Title: {title}, URL: {url}')
