
# Sample dictionary object
obj_1 = {
    u'd': {
        u'results': [
            {
                u'Desc': u'This is a description...',
                u'Title': u'This is a title...',
                u'data': {u'Url': u'www.site.com'}
            },
            {
                u'Desc': u'This is a description...',
                u'Title': u'This is a title...',
                u'data': {u'Url': u'www.site.com'}
            }
        ]
    }
}

# Extracting Title values and URLs
titles = []
urls = []

# Iterate through the results in the dictionary
for result in obj_1[u'd'][u'results']:
    titles.append(result[u'Title'])  # Collecting Title values
    urls.append(result[u'data'][u'Url'])  # Collecting URLs

# Output the extracted values
print("Titles:", titles)
print("URLs:", urls)
