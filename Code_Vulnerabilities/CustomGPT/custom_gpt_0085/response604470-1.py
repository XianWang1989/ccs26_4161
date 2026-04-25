
import re

# Sample HTML string
html_string = """
<p>Cash nbs $13,000</p>
<p>Total expenses $336,008</p>
<p>Cash and other costs $200</p>
<p>Not relevant text.</p>
"""

# Regex pattern
pattern = r"<p>(?:.*?(\bCash\b).*?(?:\$([\d,]+))?)</p>"

# Find all matches
matches = re.findall(pattern, html_string)

# Extract and print results
for match in matches:
    cash_word = match[0]  # "Cash"
    amount = match[1] if match[1] else "None"  # Amount if available
    print(f"Found: {cash_word}, Amount: {amount}")
