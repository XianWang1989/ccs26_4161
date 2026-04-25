
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

# Extracting Titles and URLs
titles_urls = [(item[u'Title'], item[u'data'][u'Url']) for item in obj_1[u'd'][u'results']]

# Printing the results
for title, url in titles_urls:
    print(f"Title: {title}, URL: {url}")
