
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

# Initialize lists to hold the extracted information
titles = []
urls = []

# Loop through the results and extract titles and URLs
for result in obj_1[u'd'][u'results']:
    titles.append(result[u'Title'])
    urls.append(result[u'data'][u'Url'])

# Display the extracted titles and URLs
print("Titles:", titles)
print("URLs:", urls)
