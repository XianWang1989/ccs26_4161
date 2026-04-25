
# Sample dictionary object
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}},

            {'Desc': 'This is another description...',
             'Title': 'Another title...',
             'data': {'Url': 'www.another-site.com'}}
        ]
    }
}

# Extracting Title and URL values
titles = []
urls = []

# Accessing the 'results' key and iterating through the items
for item in obj_1['d']['results']:
    titles.append(item['Title'])  # Collect Title values
    urls.append(item['data']['Url'])  # Collect URL values

# Outputting the extracted values
print("Titles:", titles)
print("URLs:", urls)
