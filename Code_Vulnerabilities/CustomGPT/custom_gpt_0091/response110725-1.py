
# Sample dictionary object
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}},

            {'Desc': 'This is another description...',
             'Title': 'Another title...',
             'data': {'Url': 'www.anothersite.com'}}
        ]
    }
}

# Extracting Title and URL values
titles = []
urls = []

for item in obj_1['d']['results']:
    titles.append(item['Title'])
    urls.append(item['data']['Url'])

# Outputting extracted values
print('Titles:', titles)
print('URLs:', urls)
