
import re

# Your original plot string with multiple occurrences of _choice1_ and _choice2_
plot = "This is a _choice1_ and that is also a _choice1_. Here is a _choice2_."

# Data to substitute
data1 = "apple"
data2 = "banana"

# Perform the substitutions
plot = re.sub(r'_choice1_', '%s', plot) % data1  # First substitution
plot = re.sub(r'_choice2_', '%s', plot) % data2  # Second substitution

print(plot)
