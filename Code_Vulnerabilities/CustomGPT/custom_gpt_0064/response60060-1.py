
extensionsToCheck = ['.pdf', '.doc', '.xls']
url_string = "example.pdf"

# Using any() to check if any extension is in the url_string
if any(extension in url_string for extension in extensionsToCheck):
    print(url_string)
