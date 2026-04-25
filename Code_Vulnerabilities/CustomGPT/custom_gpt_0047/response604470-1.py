
import re

# Example string to search
text = """
<p>Cash nbs $336,008</p>
<p>Cash some text not needed $13,000</p>
<p>Total $200,000</p>
<p>Cash without number</p>
"""

# Regex pattern
pattern = r'<p>\s*Cash.*?(?:\$(\d{1,3}(?:,\d{3})*)?)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Extracting "Cash" and the optional number
results = []
for match in matches:
    cash_word = "Cash"
    number = match if match else None
    results.append((cash_word, number))

# Display results
for cash, num in results:
    print(f'Word: {cash}, Number: {num}')
