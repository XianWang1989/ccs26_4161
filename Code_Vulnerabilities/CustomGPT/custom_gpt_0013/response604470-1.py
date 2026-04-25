
import re

# Sample input string
text = """
<p>Cash nbs $336,008</p>
<p>Other text Total $13,000</p>
<p>Different entry with no number</p>
<p>Cash $5,000</p>
"""

# Regular expression to match the desired pattern
pattern = r'<p>(?=.*\bCash\b)(.*?)(\$\d{1,3}(?:,\d{3})*)?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Extract "Cash" and the number
results = []
for match in matches:
    cash_text = "Cash"  # We know it starts with "Cash"
    number = match[1] if match[1] else None
    results.append((cash_text, number))

# Print the results
for cash, number in results:
    print(f'Found: "{cash}", Number: "{number}"')
