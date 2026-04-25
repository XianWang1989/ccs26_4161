
# Sample dictionary based on your structure
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title 1...',
             u'data': {u'Url': u'www.site1.com'}
            },
            {u'Desc': u'This is another description...', 
             u'Title': u'This is a title 2...',
             u'data': {u'Url': u'www.site2.com'}
            }
        ]
    }
}

# Extracting Titles and URLs
titles = [item[u'Title'] for item in obj_1[u'd'][u'results']]
urls = [item[u'data'][u'Url'] for item in obj_1[u'd'][u'results']]

# Display the results
print("Titles:", titles)
print("URLs:", urls)
