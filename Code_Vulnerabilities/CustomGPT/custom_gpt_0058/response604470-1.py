
import re

# Sample text containing the <p> tags
text = """
<p>Cash nbs $13,000</p>
<p>Total expenses were $336,008</p>
<p>Cash was spent: $336,008</p>
"""

# Regular expression pattern
pattern = r'<p>.*?(Cash)(?:.*?(\$[\d,]+))?.*?</p>'

# Find all matches using the regex
matches = re.findall(pattern, text)

# Display the results
for match in matches:
    cash_word = match[0]  # This will be 'Cash'
    amount = match[1] if match[1] else 'No amount found'
    print(f"Word: {cash_word}, Amount: {amount}")
