
import re

# Sample HTML input
html_content = "<p>Cash nbs $336,008</p>"

# Regular expression pattern
pattern = r"<p>\s*?(Cash.*?)?\$?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?\s*</p>"

# Search using regex
match = re.search(pattern, html_content)

if match:
    cash_word = match.group(1) if match.group(1) else "Cash not found"
    amount = match.group(2) if match.group(2) else "No amount found"
    print(f"Found Word: {cash_word.strip()}, Amount: {amount}")
else:
    print("No match found.")
