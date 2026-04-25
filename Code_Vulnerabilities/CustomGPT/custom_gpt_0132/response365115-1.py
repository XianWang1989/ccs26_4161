
import re

plot = "_choice1_ is red and _choice2_ is blue. _choice1_ is my favorite color."

data1 = "apple"
data2 = "sky"

# Substitute all occurrences and format the string
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use string formatting
plot = plot % (data1, data2)

print(plot)
