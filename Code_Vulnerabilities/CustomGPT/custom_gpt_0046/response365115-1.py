
import re

# Sample plot string
plot = "This is a test string with _choice1_ and _choice2_."

# Example data to substitute
data1 = "first choice"
data2 = "second choice"

# Use str.format with named placeholders
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Insert data using str.format
plot = plot.format(data1, data2)

print(plot)
