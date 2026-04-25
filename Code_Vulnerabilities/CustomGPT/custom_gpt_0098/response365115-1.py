
import re

# Sample plot string
plot = "This is a _choice1_ and another _choice2_ example with _choice1_."

# Data to substitute
data1 = "option A"
data2 = "option B"

# Use a single step to avoid chaining errors
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)
