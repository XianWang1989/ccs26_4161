
extensions_to_check = ['.pdf', '.doc', '.xls']
url_string = "example.pdf"

if any(extension in url_string for extension in extensions_to_check):
    print(url_string)
