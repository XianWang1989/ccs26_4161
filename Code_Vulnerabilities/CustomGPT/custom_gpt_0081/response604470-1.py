
import re

# Sample text containing <p> tags
text = """
<p>Cash nbs $336,008</p>
<p>Total nbs $13,000</p>
<p>Cash and some text goes here with a number $12.34</p>
<p>Just some other text</p>
"""

# Regular expression to find 'Cash' and optionally a number
pattern = r'<p>.*?\b(Cash)\b.*?(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?.*?</p>'

# Find all matches in the text
matches = re.findall(pattern, text)

# Displaying the results
for match in matches:
    cash_word = match[0]  # This will always be "Cash"
    cash_number = match[1] if match[1] else "No number found"
    print(f'Found: {cash_word}, Amount: {cash_number}')
