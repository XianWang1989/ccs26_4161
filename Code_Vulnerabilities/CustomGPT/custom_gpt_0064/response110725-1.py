
# Sample dictionary based on the provided structure
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
titles_and_urls = []
for item in obj_1['d']['results']:
    title = item['Title']
    url = item['data']['Url']
    titles_and_urls.append((title, url))

# Print results
for title, url in titles_and_urls:
    print(f'Title: {title}, URL: {url}')
