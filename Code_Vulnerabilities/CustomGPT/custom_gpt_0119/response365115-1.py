
import re

# Example data
plot = "This is _choice1_ and this is also _choice2_."
data1 = "Option 1"
data2 = "Option 2"

# Perform substitutions
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use the format method to insert the data
plot = plot % (data1, data2)

print(plot)
