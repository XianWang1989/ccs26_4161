
extensions_to_check = ['.pdf', '.doc', '.xls']
url_string = "example.pdf"

# Check if any extension is in the url_string
if any(extension in url_string for extension in extensions_to_check):
    print(url_string)
