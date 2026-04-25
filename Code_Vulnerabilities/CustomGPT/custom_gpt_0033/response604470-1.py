
import re

# Sample text
text = """
<p>Cash nbs $336,008</p>
<p>Total nbs $13,000</p>
<p>Cash nbs $13,000</p>
<p>Something else</p>
"""

# Regex pattern
pattern = r'<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*)?</p>'

# Finding all matches
matches = re.findall(pattern, text)

# Extracting and printing results
for match in matches:
    cash_word = match[0]  # This will be "Cash"
    amount = match[1] if match[1] else "No amount"
    print(f"Found: {cash_word}, Amount: {amount}")
