
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site.com'}},

            {u'Desc': u'This is a description...',
             u'Title': u'This is another title...',
             u'data': {u'Url': u'www.another-site.com'}}
        ]
    }
}

titles = [result[u'Title'] for result in obj_1[u'd'][u'results']]
urls = [result[u'data'][u'Url'] for result in obj_1[u'd'][u'results']]

print("Titles:", titles)
print("URLs:", urls)
