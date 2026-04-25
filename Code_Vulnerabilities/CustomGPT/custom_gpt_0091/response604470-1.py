
import re

# Sample input string
input_string = "<p>Cash nbs $336,008</p>"

# Regex to capture "Cash" and an optional number
pattern = r'<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Search using the regex
match = re.search(pattern, input_string)

if match:
    cash_word = match.group(1)  # "Cash"
    number = match.group(2) if match.group(2) else "No number found"
    print(f"Extracted: {cash_word}, Number: {number}")
else:
    print("No match found.")
