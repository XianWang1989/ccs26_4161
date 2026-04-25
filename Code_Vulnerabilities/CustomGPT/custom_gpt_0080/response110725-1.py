
# Sample object structure
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
titles_and_urls = []
for item in obj_1[u'd'][u'results']:
    title = item[u'Title']
    url = item[u'data'][u'Url']
    titles_and_urls.append((title, url))

# Output the results
for title, url in titles_and_urls:
    print(f"Title: {title}, URL: {url}")
