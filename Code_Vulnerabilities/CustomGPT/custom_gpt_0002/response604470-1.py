
import re

# Sample string containing <p> tags
text = "<p>Cash nbs $336,008</p>"

# Regex pattern to match "Cash" and an optional number
pattern = r'<p>\s*(Cash.*?)?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Perform the regex search
match = re.search(pattern, text)

if match:
    cash_word = match.group(1) or "No cash word found."
    amount = match.group(2) or "No amount found."
    print(f"Cash word: {cash_word.strip()}")
    print(f"Amount: {amount}")
else:
    print("No match found.")
