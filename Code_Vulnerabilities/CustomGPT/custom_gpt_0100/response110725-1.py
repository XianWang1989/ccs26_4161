
# Sample dictionary object
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}}
        ]
    }
}

# Extracting Titles and URLs
titles_and_urls = []

for result in obj_1[u'd'][u'results']:
    title = result[u'Title']
    url = result[u'data'][u'Url']
    titles_and_urls.append((title, url))

# Displaying the extracted information
for title, url in titles_and_urls:
    print(f'Title: {title}, URL: {url}')
