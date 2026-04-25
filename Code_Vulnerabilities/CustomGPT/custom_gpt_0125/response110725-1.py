
# Sample Dictionary
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

# Extracting Title and URL
titles_urls = [
    (result[u'Title'], result[u'data'][u'Url']) 
    for result in obj_1[u'd'][u'results']
]

# Printing the results
for title, url in titles_urls:
    print(f'Title: {title}, URL: {url}')
