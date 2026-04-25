
extensions_to_check = ['.pdf', '.doc', '.xls']
url_string = "example.document.pdf"

# Check if any extension is in the url_string
if any(ext in url_string for ext in extensions_to_check):
    print(url_string)
