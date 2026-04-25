
# Sample dictionary object
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}}
        ]
    }
}

# Extracting Title values and Url values
titles = [result[u'Title'] for result in obj_1[u'd'][u'results']]
urls = [result[u'data'][u'Url'] for result in obj_1[u'd'][u'results']]

# Printing out the extracted values
print("Titles:", titles)
print("URLs:", urls)
