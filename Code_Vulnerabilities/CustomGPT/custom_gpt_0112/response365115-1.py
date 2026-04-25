
import re

# Example data
data1 = "Option A"
data2 = "Option B"
plot = "_choice1_ and _choice2_ are here. _choice1_ is repeated."

# Substitute all occurrences
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use the % operator to substitute values
plot = plot % (data1, data2)

print(plot)
