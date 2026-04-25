
# Sample dictionary
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}},
            {'Desc': 'This is another description...',
             'Title': 'Another title...',
             'data': {'Url': 'www.site.com'}}
        ]
    }
}

# Extracting titles and URLs
titles_and_urls = []
for result in obj_1['d']['results']:
    title = result['Title']
    url = result['data']['Url']
    titles_and_urls.append({'Title': title, 'Url': url})

# Output the extracted values
for item in titles_and_urls:
    print(f"Title: {item['Title']}, URL: {item['Url']}")
