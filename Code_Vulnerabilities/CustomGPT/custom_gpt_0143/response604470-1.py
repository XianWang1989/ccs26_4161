
import re

# Sample HTML string
html_content = """
<p>Cash nbs $13,000</p>
<p>begins with the word "Cash" has some stuff I don't want then a number $336,008.</p>
"""

# Regular expression to extract 'Cash' and optionally a number
pattern = r'<p>(.*?Cash.*?)?(?:.*?(\$\d{1,3}(?:,\d{3})*))?</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Process the matches to extract desired values
results = []
for match in matches:
    cash_word = match[0] if match[0] else None
    number = match[1] if match[1] else None
    if cash_word:
        results.append((cash_word.strip(), number))

# Display the results
for cash, num in results:
    print(f"Found: '{cash}', Number: '{num}'")
