
# Sample dictionary object
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...', u'Title': u'This is another title...', u'data': {u'Url': u'www.another-site.com'}}
        ]
    }
}

# Extract Titles and URLs
titles = []
urls = []

for item in obj_1[u'd'][u'results']:
    titles.append(item[u'Title'])
    urls.append(item[u'data'][u'Url'])

# Display results
print("Titles:", titles)
print("URLs:", urls)
