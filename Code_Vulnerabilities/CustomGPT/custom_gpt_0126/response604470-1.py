
import re

# Sample HTML input
html_content = """
<p>Cash nbs $13,000</p>
<p>Total amount $200,000</p>
<p>Cash deal for $336,008</p>
<p>Some other text</p>
"""

# Regex pattern to find "Cash" and the optional number
pattern = r'<p>.*?(Cash.*?)\s*(.*?(\$\d{1,3}(?:,\d{3})*))?<\/p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Extracting relevant information
results = []
for match in matches:
    cash_word = match[0].strip()  # "Cash"
    number = match[2] if match[2] else None  # Number, if available
    results.append((cash_word, number))

# Printing results
for cash, num in results:
    print(f"Found: '{cash}', Amount: '{num}'")
