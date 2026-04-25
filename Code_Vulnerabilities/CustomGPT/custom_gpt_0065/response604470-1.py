
import re

# Sample text
text = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r'<p>\s*Cash.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Finding matches
match = re.search(pattern, text)

if match:
    cash_word = "Cash"
    amount = match.group(1) if match.group(1) else "Not available"
    print(f"Extracted: {cash_word}, Amount: {amount}")
else:
    print("No match found.")
