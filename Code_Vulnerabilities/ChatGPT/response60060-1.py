
extensionsToCheck = ['.pdf', '.doc', '.xls']
url_string = "example_document.pdf"

# Using any() with a generator expression
if any(extension in url_string for extension in extensionsToCheck):
    print(url_string)
