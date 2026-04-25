
import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and another _choice1_ example for _choice2_."

# Data to substitute
data1 = "first choice"
data2 = "second choice"

# Replace placeholders using re.sub and format
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use % formatting with the data
formatted_plot = plot % (data1, data2)

print(formatted_plot)
