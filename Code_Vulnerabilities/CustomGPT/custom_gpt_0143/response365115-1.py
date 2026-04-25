
import re

# Example plot string with placeholders
plot = "This is a _choice1_ test. Let's see if _choice1_ works multiple times. _choice2_ should also be replaced."

# Data to substitute
data1 = "example1"
data2 = "example2"

# Substitute all occurrences of _choice1_ and _choice2_
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)
