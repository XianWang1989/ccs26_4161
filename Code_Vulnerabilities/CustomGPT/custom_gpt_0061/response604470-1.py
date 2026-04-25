
import re

# Sample HTML content
html_content = """
<p>Cash nbs $13,000</p>
<p>Total expenses $336,008</p>
<p>Something else</p>
<p>Cash and more stuff $336,008</p>
"""

# Regex to capture "Cash" and the optional number
pattern = r"<p>.*?(Cash).*?(\$[\d,]+)?</p>"

# Find all matches
matches = re.findall(pattern, html_content)

# Process and print the results
for match in matches:
    cash_word, number = match
    print(f"Word: {cash_word}, Number: {number if number else 'None'}")
