
import re

# Sample input string
input_string = """
<p>Cash nbs $13,000</p>
<p>Total expenses $15,200</p>
<p>Cash expenses $336,008</p>
"""

# Regular expression to match the pattern
pattern = r'<p>.*?\b(Cash)\b.*?(\$\d{1,3}(?:,\d{3})*)?.*?</p>'

# Find all matches
matches = re.findall(pattern, input_string)

# Display results
for match in matches:
    cash_word, amount = match
    print(f"Extracted: {cash_word}, Amount: {amount if amount else 'No amount available'}")
