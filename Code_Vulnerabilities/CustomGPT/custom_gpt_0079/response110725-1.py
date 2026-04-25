
# Sample dictionary similar to your obj_1
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}},
            {'Desc': 'This is another description...',
             'Title': 'This is another title...',
             'data': {'Url': 'www.site2.com'}}
        ]
    }
}

# Extracting Title and Url values
titles_urls = [(item['Title'], item['data']['Url']) for item in obj_1['d']['results']]

# Printing the results
for title, url in titles_urls:
    print(f"Title: {title}, URL: {url}")
