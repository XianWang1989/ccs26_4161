
import re

# Example input string
input_text = """
<p>Cash nbs $13,000</p>
<p>Cash should be filtered $336,008.</p>
<p>Other content</p>
"""

# Regex pattern to match "Cash" and optionally capture a number
pattern = r'<p>.*?(Cash).*?(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?.*?</p>'

# Find all matches in the input text
matches = re.findall(pattern, input_text)

# Process matches
for match in matches:
    cash_word = match[0]  # This will be "Cash"
    amount = match[1] if match[1] else "Not found"  # Amount is optional
    print(f"Matched Word: {cash_word}, Amount: {amount}")
