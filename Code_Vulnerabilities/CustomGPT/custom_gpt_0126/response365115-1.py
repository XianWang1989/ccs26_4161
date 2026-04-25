
import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and that is a _choice2_."

# Data to substitute
data1 = "value1"
data2 = "value2"

# Using str.format for multiple substitutions
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Format the plot string with the provided data
plot = plot.format(data1, data2)

print(plot)
