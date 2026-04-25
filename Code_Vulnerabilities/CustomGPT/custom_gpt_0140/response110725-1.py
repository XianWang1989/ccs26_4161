
# Sample dictionary structure
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site1.com'}},
            {u'Desc': u'This is another description...',
             u'Title': u'This is another title...',
             u'data': {u'Url': u'www.site2.com'}}
        ]
    }
}

# Extracting titles and URLs
titles = []
urls = []

for result in obj_1[u'd'][u'results']:
    titles.append(result[u'Title'])
    urls.append(result[u'data'][u'Url'])

# Display the extracted values
print("Titles:", titles)
print("URLs:", urls)
