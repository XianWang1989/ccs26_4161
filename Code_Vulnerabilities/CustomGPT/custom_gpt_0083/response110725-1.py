
# Sample dictionary object
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

# Extract titles and URLs
titles = []
urls = []

for result in obj_1[u'd'][u'results']:
    titles.append(result[u'Title'])
    urls.append(result[u'data'][u'Url'])

# Print the results
print("Titles:", titles)
print("URLs:", urls)
