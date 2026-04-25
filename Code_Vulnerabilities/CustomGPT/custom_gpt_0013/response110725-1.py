
# Sample dictionary similar to obj_1
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

# Extracting Title and Url values
titles_and_urls = []
for result in obj_1['d']['results']:
    title = result['Title']
    url = result['data']['Url']
    titles_and_urls.append({'Title': title, 'Url': url})

# Outputting the results
for item in titles_and_urls:
    print(f"Title: {item['Title']}, Url: {item['Url']}")
