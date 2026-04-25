
import re

# Sample plot string with placeholders
plot = "This is a test for _choice1_ and another _choice2_."

# Data to replace the placeholders
data1 = "first choice"
data2 = "second choice"

# Use re.sub to replace placeholders
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Format the string with the data
plot = plot.format(data1, data2)

print(plot)
