
import re

# Sample plot string with multiple placeholders
plot = "This is a _choice1_ and another _choice1_. Also, this is a _choice2_."

# Data to substitute
data1 = "apple"
data2 = "orange"

# Using re.sub to replace multiple occurrences
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)
