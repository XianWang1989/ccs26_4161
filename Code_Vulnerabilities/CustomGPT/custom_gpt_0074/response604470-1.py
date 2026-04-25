
import re

# Sample input string
text = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r'<p>\s*Cash\s.*?(\$[\d{1,3}(?:,\d{3})*])?\s*</p>'

# Perform regex search
match = re.search(pattern, text)

if match:
    cash_word = "Cash"
    # Optional capturing group for the number
    amount = match.group(1) if match.group(1) else "No amount found"
    print(f"Extracted word: {cash_word}")
    print(f"Extracted amount: {amount}")
else:
    print("No match found.")
