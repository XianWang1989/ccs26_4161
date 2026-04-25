
# Assuming obj_1 is defined as mentioned
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...',
             u'Title': u'This is a title...',
             u'data': {u'Url': u'www.site1.com'}},
            {u'Desc': u'This is another description...', 
             u'Title': u'Another title...',
             u'data': {u'Url': u'www.site2.com'}}
        ]
    }
}

# Extracting Titles and URLs
titles_and_urls = []
for result in obj_1[u'd'][u'results']:
    title = result[u'Title']
    url = result[u'data'][u'Url']
    titles_and_urls.append((title, url))

# Display the extracted Titles and URLs
for title, url in titles_and_urls:
    print(f'Title: {title}, URL: {url}')
