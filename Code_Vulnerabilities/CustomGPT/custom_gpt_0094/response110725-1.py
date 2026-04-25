
# Sample dictionary
obj_1 = {
    'd': {
        'results': [
            {'Desc': 'This is a description...',
             'Title': 'This is a title...',
             'data': {'Url': 'www.site.com'}},

            {'Desc': 'This is a description...', 
             'Title': 'This is another title...',
             'data': {'Url': 'www.site2.com'}}
        ]
    }
}

# Extracting Titles and URLs
titles = [item['Title'] for item in obj_1['d']['results']]
urls = [item['data']['Url'] for item in obj_1['d']['results']]

# Displaying the results
print("Titles:", titles)
print("URLs:", urls)
