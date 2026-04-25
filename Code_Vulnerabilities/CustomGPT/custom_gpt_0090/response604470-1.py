
import re

text = """
<p>begins with the word "Cash" has some stuff I don't want then a number $336,008.</p>
<p>Cash nbs $13,000</p>
"""

# Define the regex pattern
pattern = r'<p>.*?(Cash).*?(?:\$([\d,]+))?.*?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Extract the results
results = [(match[0], match[1] if match[1] else None) for match in matches]

print(results)
