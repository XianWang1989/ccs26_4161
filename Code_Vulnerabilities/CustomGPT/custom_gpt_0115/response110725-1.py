
# Sample dictionary object
obj_1 = {
    'd': {
        'results': [
            {
                'Desc': 'This is a description...',
                'Title': 'This is a title...',
                'data': {'Url': 'www.site.com'}
            },
            {
                'Desc': 'This is a description...',
                'Title': 'This is a title...',
                'data': {'Url': 'www.site.com'}
            }
        ]
    }
}

# Extracting Title and URL
titles = []
urls = []

for result in obj_1['d']['results']:
    titles.append(result['Title'])
    urls.append(result['data']['Url'])

# Printing the results
print("Titles:", titles)
print("URLs:", urls)
