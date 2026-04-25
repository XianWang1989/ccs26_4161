
import re

# Sample HTML string
html_string = "<p>Cash nbs $336,008</p>"

# Define the regex pattern
pattern = r'<p>(.*?Cash.*?)?(?:.*?(\$[\d,]+))?<\/p>'

# Search for matches
match = re.search(pattern, html_string)

if match:
    # Extracting "Cash" and the number if available
    cash = match.group(1) or "Not found"
    number = match.group(2) or "Not found"

    print(f"Found: {cash.strip()}")
    print(f"Number: {number.strip()}")
else:
    print("No match found.")
