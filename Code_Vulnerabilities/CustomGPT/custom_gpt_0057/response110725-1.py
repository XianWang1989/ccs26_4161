
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}}
        ]
    }
}

titles = [item[u'Title'] for item in obj_1[u'd'][u'results']]
urls = [item[u'data'][u'Url'] for item in obj_1[u'd'][u'results']]

print("Titles:", titles)
print("URLs:", urls)
