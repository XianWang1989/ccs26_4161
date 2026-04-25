
# Assume obj_1 is your dictionary
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}},

            {'Desc': 'This is a description...',
             'Title': 'This is another title...',
             'data': {'Url': 'www.another-site.com'}}
        ]
    }
}

# Extract Titles and URLs
titles_urls = []
for item in obj_1['d']['results']:
    title = item['Title']
    url = item['data']['Url']
    titles_urls.append({'Title': title, 'Url': url})

# Print the extracted values
for entry in titles_urls:
    print(f"Title: {entry['Title']}, URL: {entry['Url']}")
