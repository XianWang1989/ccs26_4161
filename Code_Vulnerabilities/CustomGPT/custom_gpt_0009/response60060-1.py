
extensionsToCheck = ['.pdf', '.doc', '.xls']
url_string = "example.pdf"  # replace this with your actual string

if any(extension in url_string for extension in extensionsToCheck):
    print(url_string)
