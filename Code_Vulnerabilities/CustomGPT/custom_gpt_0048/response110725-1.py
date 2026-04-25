
# Sample dictionary object
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}
            },
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}
            }
        ]
    }
}

# Extracting Title and URL values
titles = []
urls = []

for result in obj_1['d']['results']:
    titles.append(result['Title'])  # Get Title
    urls.append(result['data']['Url'])  # Get URL

# Output the results
print("Titles:", titles)
print("URLs:", urls)
