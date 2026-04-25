
# Given dictionary object
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}},

            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}}
        ]
    }
}

# Extracting Titles and URLs
titles = []
urls = []

for item in obj_1['d']['results']:
    titles.append(item['Title'])            # Extract Title
    urls.append(item['data']['Url'])        # Extract URL

# Printing the results
print("Titles:", titles)
print("URLs:", urls)
