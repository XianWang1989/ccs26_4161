
import re

# Example data
plot = "This is a _choice1_ and here is another _choice1_ and also a _choice2_."
data1 = "apple"
data2 = "banana"

# Using re.sub to substitute all occurrences
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Applying the substitutions
plot = plot.format(data1, data2)

print(plot)
