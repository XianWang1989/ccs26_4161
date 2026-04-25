
import re

plot = "This is a _choice1_ and also a _choice2_. Here is another _choice1_."

# Example data for substitution
data1 = "Apple"
data2 = "Orange"

# Using re.sub to replace all occurrences
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Formatting the string with data
plot = plot % (data1, data2)

print(plot)
