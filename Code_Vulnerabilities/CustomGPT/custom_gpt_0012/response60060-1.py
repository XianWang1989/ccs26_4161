
extensionsToCheck = ['.pdf', '.doc', '.xls']
url_string = 'example.doc'

if any(extension in url_string for extension in extensionsToCheck):
    print(url_string)
