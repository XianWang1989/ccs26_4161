
import re

# Sample plot string with placeholders
plot = "This is a plot with _choice1_ and _choice2_, and again _choice1_."

# Values to substitute
data1 = "Option1"
data2 = "Option2"

# Substitute using regex and format
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Use str.format to substitute values
plot = plot.format(data1, data2)

print(plot)
