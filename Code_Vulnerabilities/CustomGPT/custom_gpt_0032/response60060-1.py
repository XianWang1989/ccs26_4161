
extensionsToCheck = ['.pdf', '.doc', '.xls']
url_string = "example_file.pdf"

if any(extension in url_string for extension in extensionsToCheck):
    print(url_string)
