
# Sample dictionary structure similar to your obj_1
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...', 
             'Title': 'This is a title...', 
             'data': {'Url': 'www.site1.com'}},
            {'Desc': 'This is another description...', 
             'Title': 'This is another title...', 
             'data': {'Url': 'www.site2.com'}}
        ]
    }
}

# Extracting Titles and URLs
titles = []
urls = []

for result in obj_1['d']['results']:
    titles.append(result['Title'])
    urls.append(result['data']['Url'])

print("Titles:", titles)
print("URLs:", urls)
