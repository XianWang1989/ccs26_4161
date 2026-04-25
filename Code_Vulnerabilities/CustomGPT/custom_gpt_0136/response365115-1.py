
import re

# Sample plot string with multiple occurrences
plot = "This is a _choice1_ and this is another _choice1_. Also, a _choice2_ here."

data1 = "variable1"
data2 = "variable2"

# Substitute all occurrences
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use % formatting once to inject all variables
plot = plot % (data1, data2)

print(plot)
