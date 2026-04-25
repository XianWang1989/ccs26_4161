# Sample dictionary (decoded JSON)
obj_1 = {
    'd': {
        'results': [
            {
                'Desc': 'This is a description...',
                'Title': 'This is a title...',
                'data': {'Url': 'www.site.com'}
            },
            {
                'Desc': 'This is a description...',
                'Title': 'This is a title...',
                'data': {'Url': 'www.site.com'}
            }
        ]
    }
}

# Extracting Title and Url
for item in obj_1['d']['results']:
    title = item.get('Title')
    url = item.get('data', {}).get('Url')
    print(f"Title: {title}, URL: {url}")
