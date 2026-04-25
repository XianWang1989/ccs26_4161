
import re

# Sample input string containing the HTML
html_string = "<p>Cash nbs $13,000</p>"

# Regular expression to match 'Cash' and an optional number
# This captures the word 'Cash' using the non-capturing group (?:)
# It looks for an optional amount that starts with a dollar sign followed by digits and commas
pattern = r"<p>(?:.*?\bCash\b.*?)(?:\$(\d{1,3}(?:,\d{3})*))?.*?</p>"

# Search for the pattern
match = re.search(pattern, html_string)

if match:
    cash_found = "Cash" if "Cash" in match.group(0) else None
    amount_found = match.group(1) if match.group(1) else None
    print(f"Caught: {cash_found}, Amount: ${amount_found if amount_found else 'Not found'}")
else:
    print("No match found.")
