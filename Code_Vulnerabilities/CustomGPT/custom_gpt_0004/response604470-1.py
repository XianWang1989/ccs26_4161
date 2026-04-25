
import re

# Sample input HTML
text = """
<p>Cash nbs $336,008</p>
<p>Not interested</p>
<p>Cash some more stuff $13,000</p>
"""

# Regex pattern to extract "Cash" and the optional number
pattern = r'<p>(.*?)Cash.*?(?:\$([\d,]+))?.*?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Process and display results
results = [(match[0].strip(), match[1]) for match in matches if match[0]]
for result in results:
    cash_found = result[0]
    number_found = result[1] if result[1] else "No amount found"
    print(f"Extracted: '{cash_found}', Amount: '{number_found}'")
