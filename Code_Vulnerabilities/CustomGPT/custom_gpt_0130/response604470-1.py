
import re

# Sample HTML-like string
text = """
<p>Cash nbs $13,000</p>
<p>Other text Total $336,008</p>
<p>Cash some other information $336,008</p>
"""

# Regex to match <p> tags containing "Cash" followed by optional text and a number
pattern = r'<p>(.*?)Cash.*?(\$[\d,]+)?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Process and print results
for match in matches:
    cash_word = "Cash"       # Fixed word we want
    amount = match[1] if match[1] else "No number"
    print(f'Found: {cash_word}, Amount: {amount}')
