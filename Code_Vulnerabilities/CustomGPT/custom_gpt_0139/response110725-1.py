
# Assume obj_1 is defined as below
obj_1 = {
    u'd': {
        u'results': [
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}},
            {u'Desc': u'This is a description...', u'Title': u'This is a title...', u'data': {u'Url': u'www.site.com'}}
        ]
    }
}

# Initialize empty lists to hold extracted information
titles = []
urls = []

# Loop through each result in the results list
for result in obj_1[u'd'][u'results']:
    # Extract the Title and Url for each result
    title = result[u'Title']
    url = result[u'data'][u'Url']

    # Append the extracted values to the lists
    titles.append(title)
    urls.append(url)

# Output the extracted Titles and URLs
print("Titles:", titles)
print("URLs:", urls)
