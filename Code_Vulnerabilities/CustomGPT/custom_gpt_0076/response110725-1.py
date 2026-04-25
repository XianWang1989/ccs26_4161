
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

# Initialize lists to hold Titles and URLs
titles = []
urls = []

# Extract Titles and URLs
for item in obj_1[u'd'][u'results']:
    titles.append(item[u'Title'])
    urls.append(item[u'data'][u'Url'])

# Output the results
print("Titles:", titles)
print("URLs:", urls)
