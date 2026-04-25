
import re

text = "<p>Cash nbs $13,000</p>"

# Regex pattern to match 'Cash' and the number after it
pattern = r'<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Search using the regex
match = re.search(pattern, text)

if match:
    cash_word = match.group(1)  # "Cash"
    cash_amount = match.group(2)  # "$13,000" or None
    print(f"Word: {cash_word}")
    if cash_amount:
        print(f"Amount: {cash_amount}")
    else:
        print("Amount: None")
else:
    print("No match found.")
