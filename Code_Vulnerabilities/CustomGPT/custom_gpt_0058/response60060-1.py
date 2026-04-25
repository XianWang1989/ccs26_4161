
extensionsToCheck = ['.pdf', '.doc', '.xls']
url_string = 'example.pdf'  # Replace this with your actual URL string

if any(extension in url_string for extension in extensionsToCheck):
    print(url_string)
