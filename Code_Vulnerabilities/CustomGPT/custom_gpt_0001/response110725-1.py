
# Sample dictionary similar to obj_1
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}
            },
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}
            }
        ]
    }
}

# Initialize lists to store the extracted titles and URLs
titles = []
urls = []

# Iterate through the results in the dictionary
for result in obj_1[u'd'][u'results']:
    titles.append(result[u'Title'])  # Extract Title
    urls.append(result[u'data'][u'Url'])  # Extract Url

# Print the extracted titles and urls
print("Titles:", titles)
print("URLs:", urls)
