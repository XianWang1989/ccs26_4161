
# Sample dictionary object
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}},

            {'Desc': 'This is a description...',
             'Title': 'Another title...',
             'data': {'Url': 'www.site2.com'}}
        ]
    }
}

# Extracting Title and URL values
titles_urls = [(result['Title'], result['data']['Url']) for result in obj_1['d']['results']]

# Output the extracted values
for title, url in titles_urls:
    print(f'Title: {title}, URL: {url}')
