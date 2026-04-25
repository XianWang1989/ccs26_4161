
import re

# Example plot string with multiple occurrences
plot = "This is a _choice1_ and here is another _choice1_ along with _choice2_."

# Data to substitute
data1 = "option A"
data2 = "option B"

# Substitute all occurrences for _choice1_ and _choice2_
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)
