
# Sample dictionary
obj_1 = {
    u'd': {
        u'results': [
            {
                u'Desc': u'This is a description...',
                u'Title': u'This is a title 1...',
                u'data': {u'Url': u'www.site1.com'}
            },
            {
                u'Desc': u'This is a description...',
                u'Title': u'This is a title 2...',
                u'data': {u'Url': u'www.site2.com'}
            }
        ]
    }
}

# Extracting Titles and URLs
titles = []
urls = []

for result in obj_1[u'd'][u'results']:
    titles.append(result[u'Title'])
    urls.append(result[u'data'][u'Url'])

# Output the results
print("Titles:", titles)
print("URLs:", urls)
