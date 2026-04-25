
extensions_to_check = ['.pdf', '.doc', '.xls']
url_string = "example_document.pdf"

# Check if any of the extensions are in the url_string
if any(extension in url_string for extension in extensions_to_check):
    print(url_string)
