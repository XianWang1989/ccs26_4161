
import re

# Sample HTML input
text = """
<p>Cash nbs $13,000</p>
<p>Total amount due $336,008</p>
<p>Cash something else $336,008</p>
<p>Not relevant text</p>
"""

# Regular expression to match the desired content
pattern = r'<p>\s*?(Cash)(?:(?!<\/p>).)*?(\$\d{1,3}(?:,\d{3})*)?\s*?<\/p>'

# Find all matches
matches = re.findall(pattern, text)

# Process and display results
for match in matches:
    cash_word = match[0]  # This will be "Cash"
    amount = match[1] if match[1] else "No amount found"
    print(f"Found: '{cash_word}' and '{amount}'")
