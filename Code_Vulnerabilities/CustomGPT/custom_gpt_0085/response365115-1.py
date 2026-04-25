
import re

# Sample plot string with multiple placeholders
plot = "This is a _choice1_ and another _choice1_. And here is a _choice2_."

# Data for substitution
data1 = "apple"
data2 = "banana"

# Substitute all occurrences
plot = re.sub(r'_choice1_', '%s', plot) % (data1,)
plot = re.sub(r'_choice2_', '%s', plot) % (data2,)

# Print the result
print(plot)
