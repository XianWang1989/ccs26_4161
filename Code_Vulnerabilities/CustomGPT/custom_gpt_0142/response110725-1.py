
# Sample dictionary object
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

# Extracting Titles and URLs
titles = []
urls = []

for result in obj_1[u'd'][u'results']:
    titles.append(result[u'Title'])  # Extracting Title
    urls.append(result[u'data'][u'Url'])  # Extracting URL

# Output the results
print("Titles:", titles)
print("URLs:", urls)
