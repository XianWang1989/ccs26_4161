
import re

text = "<p>Cash nbs $336,008</p>"
match = re.search(r'<p>(.*?)</p>', text)
if match:
    print(match.group(1))  # Outputs: Cash nbs $336,008
