
# Given dictionary
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}}
        ]
    }
}

# Lists to hold the extracted values
titles = []
urls = []

# Extracting Title and URL values
for result in obj_1[u'd'][u'results']:
    titles.append(result[u'Title'])
    urls.append(result[u'data'][u'Url'])

# Printing the results
print("Titles:", titles)
print("URLs:", urls)
