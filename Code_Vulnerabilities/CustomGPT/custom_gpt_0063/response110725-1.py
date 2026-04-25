
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}},

            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}}
        ]
    }
}

# Initialize lists to hold the extracted titles and URLs
titles = []
urls = []

# Loop through the results
for item in obj_1[u'd'][u'results']:
    titles.append(item[u'Title'])
    urls.append(item[u'data'][u'Url'])

# Print the extracted values
print("Titles:", titles)
print("URLs:", urls)
