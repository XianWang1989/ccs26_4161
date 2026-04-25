
import re

# Example plot string with placeholders
plot = "This is a plot with _choice1_ and _choice2_ that repeats _choice1_ multiple times."

# Data to substitute
data1 = "Option A"
data2 = "Option B"

# Using re.sub for substitution
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Now use str.format to replace the placeholders
plot = plot % (data1, data2)

# Print result
print(plot)
