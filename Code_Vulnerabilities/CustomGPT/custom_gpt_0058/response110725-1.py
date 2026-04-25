
# Your dictionary object
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}}
        ]
    }
}

# Extracting the Title and URL values
titles = []
urls = []
for item in obj_1[u'd'][u'results']:
    titles.append(item[u'Title'])
    urls.append(item[u'data'][u'Url'])

# Displaying the extracted values
print("Titles:", titles)
print("URLs:", urls)
