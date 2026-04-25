
import re

# Example plot string
plot = "This is a test with _choice1_ and _choice2_ and another _choice1_."

# Data to replace with
data1 = "Option A"
data2 = "Option B"

# Substitute all occurrences
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use % formatting to replace the placeholders
plot = plot % (data1, data2)

print(plot)
