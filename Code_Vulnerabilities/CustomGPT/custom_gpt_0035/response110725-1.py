
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}}
        ]
    }
}

# Extract Titles and URLs
titles_and_urls = [
    {
        'Title': result[u'Title'],
        'Url': result[u'data'][u'Url']
    }
    for result in obj_1[u'd'][u'results']
]

print(titles_and_urls)
