
import re

# Sample HTML input
html_content = """
<p>Cash nbs $13,000</p>
<p>Total revenue is $336,008</p>
<p>Something else</p>
"""

# Define the regex to find the <p> tags and capture required content
pattern = r'<p>(.*?\bCash\b.*?)(\$[\d,]+)?</p>'

# Find all matches in the html content
matches = re.findall(pattern, html_content)

# Process the matches to extract the desired information
results = []
for match in matches:
    cash_part = match[0]  # First capturing group (the text containing "Cash")
    number_part = match[1] if match[1] else ''  # Second capturing group (the number)

    # Clean up the captured text
    cleaned_cash_part = cash_part.replace('<p>', '').replace('</p>', '').strip()
    results.append((cleaned_cash_part, number_part))

# Print the results
for cash, number in results:
    print(f'Cash Part: "{cash}", Number: "{number}"')
