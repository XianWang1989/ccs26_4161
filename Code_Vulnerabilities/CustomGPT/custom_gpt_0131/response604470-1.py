
import re

text = "<p>Cash nbs $336,008</p>"
pattern = r"<p>\s*(Cash)\s*(?:.*?)(\$\d{1,3}(?:,\d{3})*)?\s*</p>"

match = re.search(pattern, text)
if match:
    cash_term = match.group(1)  # Will capture "Cash"
    cash_amount = match.group(2) if match.group(2) else "No amount found"  # Optional capture of the amount
    print(f"Term: {cash_term}, Amount: {cash_amount}")
else:
    print("No match found.")
