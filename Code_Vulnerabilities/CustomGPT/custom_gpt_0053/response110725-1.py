
# Assuming obj_1 is defined as given in your question
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is another description...', 
             u'Title': u'Another title...',
             u'data': {u'Url': u'www.another-site.com'}}
        ]
    }
}

# Extracting Titles and URLs
titles_urls = []
for result in obj_1[u'd'][u'results']:
    title = result[u'Title']
    url = result[u'data'][u'Url']

    titles_urls.append((title, url))

# Printing the extracted titles and URLs
for title, url in titles_urls:
    print(f'Title: {title}, URL: {url}')
