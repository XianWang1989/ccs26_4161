
import re

# Sample plot string
plot = "This is a _choice1_ and another _choice2_."

# Data to replace
data1 = "apple"
data2 = "banana"

# Perform substitutions
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Final formatting with data
plot = plot % (data1, data2)

print(plot)
