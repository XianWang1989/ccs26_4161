
import re

# Example data
plot = "This is a _choice1_ and that is a _choice2_. _choice1_ again!"
data1 = "apple"
data2 = "banana"

# Substitute placeholders with %s
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use the % operator for formatting after substitutions
plot = plot % (data1, data2)

print(plot)
