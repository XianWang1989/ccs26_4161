
import re

# Sample plot string with placeholders
plot = "This is a plot with _choice1_ and _choice2_"

# Data to substitute
data1 = "Option A"
data2 = "Option B"

# Use str.format() for multiple substitutions
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Substitute with .format()
plot = plot.format(data1, data2)

print(plot)
