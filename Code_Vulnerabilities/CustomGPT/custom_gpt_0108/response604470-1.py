
import re

# Sample input string
text = "<p>Cash nbs $336,008</p>"

# Regular expression to match the content
pattern = r"<p>(.*?Cash.*?)\s*(\$[\d,]+)?<\/p>"

# Perform the search
match = re.search(pattern, text)

if match:
    cash_word = match.group(1)
    number = match.group(2) if match.group(2) else "Not found"

    print(f"Extracted Word: {cash_word}")
    print(f"Extracted Number: {number}")
else:
    print("No match found.")
