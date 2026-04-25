
import re

# Sample input string
text = """
<p>Cash nbs $13,000</p>
<p>Total $336,008</p>
<p>Cash stuff $336,008</p>
<p>Unrelated text</p>
"""

# Regular expression pattern
pattern = r'<p>(.*?\bCash\b.*?)(?:\$([\d,]+))?.*?<\/p>'

# Finding all matches
matches = re.findall(pattern, text)

# Extracting and printing results
for match in matches:
    cash_text, amount = match
    amount = amount if amount else "N/A"  # Handle case where amount is not found
    print(f"Found: '{cash_text.strip()}' with amount: {amount}")
