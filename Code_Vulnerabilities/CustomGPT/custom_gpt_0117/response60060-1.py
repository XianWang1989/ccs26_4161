
extensionsToCheck = ['.pdf', '.doc', '.xls']
url_string = "example.document.doc"  # Example URL string

if any(extension in url_string for extension in extensionsToCheck):
    print(url_string)
