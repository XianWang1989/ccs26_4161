
import re

# Sample HTML input
html_content = """
<p>Cash nbs $13,000</p>
<p>Total savings $336,008</p>
<p>Cash is important</p>
<p>Expenses $45,000</p>
"""

# Regex pattern to extract "Cash" and an optional monetary value
pattern = r'<p>(.*?)Cash.*?(?:\$(\d{1,3}(?:,\d{3})*))?</p>'

# Finding all matches
matches = re.findall(pattern, html_content)

# Processing matches
results = []
for match in matches:
    cash = "Cash"  # Since "Cash" is always captured
    number = match[1] if match[1] else None
    results.append((cash, number))

# Display results
for cash, number in results:
    print(f"Found: {cash}, Amount: {number if number else 'N/A'}")
