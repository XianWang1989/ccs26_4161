
import re

# Example data
plot = "This is a _choice1_ and another _choice1_ and _choice2_."
data1 = "apple"
data2 = "banana"

# Replace all occurrences
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use a single format operation
plot = plot % (data1, data2)

print(plot)
