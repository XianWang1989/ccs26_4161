
import re

# Sample HTML content.
html_content = "<p>Cash nbs $336,008</p>"

# Regex pattern.
pattern = r"<p>\s*(Cash)\s.*?(\$[\d{1,3}(,\d{3})*])?\s*</p>"

# Perform the search.
match = re.search(pattern, html_content)

# Check if we found a match and print the results.
if match:
    cash_word = match.group(1)  # "Cash"
    cash_amount = match.group(2) if match.group(2) else "No amount found"
    print(f"Extracted: {cash_word}, Amount: {cash_amount}")
else:
    print("No match found.")
