
import re

# Sample HTML content
html_content = "<p>Cash nbs $336,008</p>"

# Regular expression to capture "Cash" and the number
pattern = r'<p>\s*(Cash)\s*.*?(\$[\d,]+)?\s*</p>'

# Search the content
match = re.search(pattern, html_content)

if match:
    cash_word = match.group(1)  # This will get "Cash"
    amount = match.group(2) if match.group(2) else "No amount found"  # This will get the number if available
    print(f"Extracted: {cash_word}, Amount: {amount}")
else:
    print("No match found")
