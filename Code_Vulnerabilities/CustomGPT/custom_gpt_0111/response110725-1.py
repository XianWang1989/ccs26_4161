
# Sample dictionary object
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}},
            {'Desc': 'This is another description...',
             'Title': 'This is another title...',
             'data': {'Url': 'www.another-site.com'}}
        ]
    }
}

# Extracting Titles and URLs
titles_urls = [(result['Title'], result['data']['Url']) for result in obj_1['d']['results']]

# Display the results
for title, url in titles_urls:
    print(f'Title: {title}, URL: {url}')
