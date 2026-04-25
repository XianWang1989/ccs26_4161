
# Given dictionary object
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}}
        ]
    }
}

# Extract Title and Url values
titles = []
urls = []

for result in obj_1[u'd'][u'results']:
    titles.append(result[u'Title'])  # Extract Title
    urls.append(result[u'data'][u'Url'])  # Extract Url

# Output the results
print("Titles:", titles)
print("URLs:", urls)
