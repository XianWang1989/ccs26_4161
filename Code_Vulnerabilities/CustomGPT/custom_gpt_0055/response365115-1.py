
import re

# Sample plot string and data
plot = "This is a _choice1_ and this is also a _choice1_ and _choice2_."
data1 = "apple"
data2 = "banana"

# Replace the placeholders
plot = re.sub(r'_choice1_', "%s", plot)
plot = re.sub(r'_choice2_', "%s", plot)

# Format with data
plot = plot % (data1, data2)

# Print the result
print(plot)
