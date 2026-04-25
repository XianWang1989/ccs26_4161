
import re

# Sample input string
text = """
<p>Cash nbs $336,008</p>
<p>Total sales $500,000</p>
<p>Other text</p>
<p>Cash flow is positive $100,000</p>
"""

# Regex pattern to match what you need
pattern = r'<p>(.*?)Cash.*?(\$\d{1,3}(?:,\d{3})*)?<\/p>'

# Find all matches
matches = re.findall(pattern, text)

# Extract and display results
for match in matches:
    cash_word = "Cash"  # Since we always want "Cash"
    amount = match[1] if match[1] else "No amount found"
    print(f'Extracted word: {cash_word}, Extracted amount: {amount}')
