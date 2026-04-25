
import re

# Sample input string
text = """<p>Cash nbs $13,000</p><p>Total sales $336,008</p>"""

# Regex pattern to match "Cash" and an optional number
pattern = r'<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Finding all matches
matches = re.findall(pattern, text)

# Displaying the results
for match in matches:
    cash_word = match[0]
    amount = match[1] if match[1] else "No amount found"
    print(f"Extracted: {cash_word}, Amount: {amount}")
