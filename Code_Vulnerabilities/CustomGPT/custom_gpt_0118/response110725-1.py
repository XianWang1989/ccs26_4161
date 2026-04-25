
# Example dictionary object
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

# Extracting Title and URL values
titles_urls = [
    {
        "Title": result[u'Title'],
        "URL": result[u'data'][u'Url']
    }
    for result in obj_1[u'd'][u'results']
]

# Printing the extracted values
for item in titles_urls:
    print(f"Title: {item['Title']}, URL: {item['URL']}")
