
# Example dictionary
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

# Extracting Titles and URLs
titles_and_urls = []
for result in obj_1[u'd'][u'results']:
    title = result[u'Title']
    url = result[u'data'][u'Url']
    titles_and_urls.append({'Title': title, 'URL': url})

# Output the extracted information
for item in titles_and_urls:
    print(f"Title: {item['Title']}, URL: {item['URL']}")
