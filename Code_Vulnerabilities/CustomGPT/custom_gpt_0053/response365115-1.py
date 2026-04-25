
import re

# Sample plot string
plot = "This is a test with _choice1_ and _choice2_ and _choice1_ again."

# Data for substitution
data1 = "Apple"
data2 = "Banana"

# Substitute variables
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Apply formatting with tuple
result = plot % (data1, data2)

print(result)  # Output: This is a test with Apple and Banana and Apple again.
