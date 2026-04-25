
import re

text = "<p>Cash nbs $336,008</p>"

# Define the regex pattern
pattern = r"<p>\s*(Cash)[^<]*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>"

# Search using the re module
match = re.search(pattern, text)

if match:
    # Extract matched groups
    cash_word = match.group(1)
    cash_amount = match.group(2) if match.group(2) else "No amount found"
    print(f"Caught: {cash_word}, Amount: {cash_amount}")
else:
    print("No match found.")
