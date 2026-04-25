
import re

# Sample HTML content
html_content = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r'<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Searching the pattern
match = re.search(pattern, html_content)

if match:
    cash_word = match.group(1)  # Getting the word "Cash"
    amount = match.group(2)      # Getting the amount if available
    print(f"Found: {cash_word}, Amount: {amount}")
else:
    print("No match found.")
