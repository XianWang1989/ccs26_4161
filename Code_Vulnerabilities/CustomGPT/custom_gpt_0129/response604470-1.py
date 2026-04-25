
import re

# Sample HTML input
html_content = """
<p>Cash nbs $336,008</p>
<p>Cash nbs $13,000</p>
<p>Total amount is $123,456</p>
<p>Item sold for $5,000</p>
"""

# Regex pattern to find "Cash" followed by optional text and a number
pattern = r'<p>(.*?)Cash.*?(\$\d{1,3}(?:,\d{3})*)?<\/p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Process and print the results
for match in matches:
    cash_value = match[0]  # The text before "Cash" (if any)
    amount = match[1]      # The dollar amount (if any)

    print(f"Cash Value: {cash_value.strip()}, Amount: {amount if amount else 'No amount found'}")
