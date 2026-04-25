
import re

# Sample plot string
plot = "This is a _choice1_ and another _choice2_ _choice1_."

# Data to substitute
data1 = "apple"
data2 = "banana"

# Using re.sub and str.format
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Formatting with str.format
plot = plot.format(data1, data2)

# Printing the result
print(plot)
