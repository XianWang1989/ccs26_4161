
import re

text = "<p>Cash nbs $336,008</p>"
pattern = r"<p>(.*?\bCash\b.*?)(?:.*?(\$\d{1,3}(?:,\d{3})*))?</p>"

match = re.search(pattern, text)
if match:
    cash = match.group(1).strip()  # This will extract "Cash" and surrounding text
    number = match.group(2) if match.group(2) else None  # This will extract the number if present
    print("Extracted:", cash)
    print("Number:", number)
else:
    print("No match found.")
