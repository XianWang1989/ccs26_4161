
import re

# Sample plot string
plot = "_choice1_ and _choice1_ is replaced, then _choice2_ here."

# Data to substitute
data1 = "value1"
data2 = "value2"

# Substitute using re.sub with lambda for multiple occurrences
plot = re.sub(r'_choice1_', lambda m: data1, plot)
plot = re.sub(r'_choice2_', lambda m: data2, plot)

print(plot)
