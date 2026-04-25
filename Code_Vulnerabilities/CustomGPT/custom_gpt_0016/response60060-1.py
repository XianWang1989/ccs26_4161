
url_string = "example.pdf"

extensions_to_check = ['.pdf', '.doc', '.xls']

if any(extension in url_string for extension in extensions_to_check):
    print(url_string)
