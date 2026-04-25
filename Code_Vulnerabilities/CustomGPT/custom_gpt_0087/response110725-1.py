
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

# Extract Titles and URLs
titles_urls = []
for result in obj_1[u'd'][u'results']:
    title = result[u'Title']
    url = result[u'data'][u'Url']
    titles_urls.append({"Title": title, "Url": url})

# Example output
for item in titles_urls:
    print(f"Title: {item['Title']}, URL: {item['Url']}")
