
import re

# Sample input string
input_string = '''
<p>Cash nbs $336,008</p>
<p>Total income $500,000</p>
<p>Cash nbs $13,000</p>
'''

# Regular expression
pattern = r'<p>\s*(Cash.*?)\s*(?:.*?)(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches using re.findall
matches = re.findall(pattern, input_string)

# Extract results
results = []
for match in matches:
    cash_word = match[0]  # This will always be "Cash"
    amount = match[1] if match[1] else "No amount found"
    results.append((cash_word, amount))

# Display results
for result in results:
    print(f'Found: {result[0]}, Amount: {result[1]}')
