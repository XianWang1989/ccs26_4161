
extensionsToCheck = ['.pdf', '.doc', '.xls']
url_string = "Here is a document.pdf that you might find useful."

# Using any() to check for any extension in the url_string
if any(extension in url_string for extension in extensionsToCheck):
    print(url_string)
