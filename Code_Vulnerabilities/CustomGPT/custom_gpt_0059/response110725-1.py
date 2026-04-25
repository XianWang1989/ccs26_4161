
# Sample dictionary object
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...', 'Title': 'This is a title...', 'data': {'Url': 'www.site.com'}},
            {'Desc': 'This is a description...', 'Title': 'This is a title...', 'data': {'Url': 'www.site.com'}}
        ]
    }
}

# Extract Title and Url values
titles_and_urls = []
for result in obj_1['d']['results']:
    title = result['Title']
    url = result['data']['Url']
    titles_and_urls.append({'Title': title, 'Url': url})

# Print the extracted values
for item in titles_and_urls:
    print(f"Title: {item['Title']}, Url: {item['Url']}")
