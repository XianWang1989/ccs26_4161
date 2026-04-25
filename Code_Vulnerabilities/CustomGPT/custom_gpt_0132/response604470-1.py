
import re

# Example input string
text = "<p>Cash nbs $336,008</p>"

# Regular expression to match the required pattern
pattern = r'<p>\s*(Cash).*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Searching for the pattern
match = re.search(pattern, text)

if match:
    cash_word = match.group(1)  # This captures "Cash"
    cash_amount = match.group(2)  # This captures the number if it exists
    print(f"Extracted: {cash_word}")
    if cash_amount:
        print(f"Amount: {cash_amount}")
else:
    print("No match found.")
