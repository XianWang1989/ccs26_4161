
extensionsToCheck = ['.pdf', '.doc', '.xls']

if any(extension in url_string for extension in extensionsToCheck):
    print(url_string)
