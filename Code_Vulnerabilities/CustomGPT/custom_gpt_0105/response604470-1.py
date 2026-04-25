
import re

text = """
<p>Cash nbs $336,008</p>
<p>Some other text</p>
<p>Cash jumbled text $13,000</p>
"""

# Regular expression pattern
pattern = r'<p>(.*?)Cash.*?(\$[\d,]+)?<\/p>'

# Find all matches
matches = re.findall(pattern, text)

# Process the results
results = []
for cash_text, amount in matches:
    results.append({
        'cash': 'Cash',
        'amount': amount if amount else 'No amount provided'
    })

# Print results
for result in results:
    print(result)
