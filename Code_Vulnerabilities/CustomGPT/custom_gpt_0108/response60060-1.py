
extensionsToCheck = ['.pdf', '.doc', '.xls']
url_string = "example.pdf"

# Check if any extension is in the URL string
if any(extension in url_string for extension in extensionsToCheck):
    print(url_string)
