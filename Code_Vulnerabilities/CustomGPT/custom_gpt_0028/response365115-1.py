
import re

# Sample plot string
plot = "This is a _choice1_ test _choice2_ with _choice1_ again."

# Data for replacements
data1 = "variable1"
data2 = "variable2"

# Substitute placeholders with '%s'
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use a tuple for formatting
plot = plot % (data1, data2)

print(plot)
