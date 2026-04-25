
import re

# Sample HTML input
html_input = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r'<p>\s*(Cash.*?)?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Searching using re module
match = re.search(pattern, html_input)

if match:
    cash_info = match.group(1)  # "Cash" and following text
    amount_info = match.group(2)  # The amount if present
    print(f"Found: {cash_info.strip() if cash_info else 'None'}")
    print(f"Amount: {amount_info if amount_info else 'None'}")
else:
    print("No match found.")
