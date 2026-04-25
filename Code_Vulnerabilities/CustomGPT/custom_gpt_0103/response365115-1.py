
import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and also a _choice2_"

# Data to substitute
data1 = "first choice"
data2 = "second choice"

# Using re.sub to replace with {} placeholders
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Formatting the string
plot = plot.format(data1, data2)

print(plot)  # Output: This is a first choice and also a second choice
