
import re

# Sample HTML content
html_content = "<p>Cash nbs $13,000</p>"

# Regex pattern to match and capture "Cash" and the optional number
pattern = r'<p>\s*(Cash)\s.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Search for matches
match = re.search(pattern, html_content)

if match:
    cash_word = match.group(1)  # "Cash"
    number = match.group(2) if match.group(2) else None  # Extracted number
    print(f"Extracted word: {cash_word}")
    print(f"Extracted number: {number}")
else:
    print("No match found.")
