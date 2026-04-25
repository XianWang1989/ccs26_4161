
# Assuming obj_1 contains your given dictionary structure
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...', 
             u'Title': u'This is a title...', 
             u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is another description...', 
             u'Title': u'Another title...', 
             u'data': {u'Url': u'www.another-site.com'}}
        ]
    }
}

# Extracting Title and Url values
titles_and_urls = []
for result in obj_1[u'd'][u'results']:
    title = result[u'Title']
    url = result[u'data'][u'Url']
    titles_and_urls.append((title, url))

# Print the extracted Title and Url values
for title, url in titles_and_urls:
    print(f'Title: {title}, URL: {url}')
