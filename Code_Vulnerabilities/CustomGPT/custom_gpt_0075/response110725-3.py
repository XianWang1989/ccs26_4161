
titles = []
urls = []

for result in obj_1[u'd'][u'results']:
    titles.append(result[u'Title'])
    urls.append(result[u'data'][u'Url'])
