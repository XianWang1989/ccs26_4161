
extensionsToCheck = ['.pdf', '.doc', '.xls']
url_string = "example.doc"

if any(ext in url_string for ext in extensionsToCheck):
    print(url_string)
