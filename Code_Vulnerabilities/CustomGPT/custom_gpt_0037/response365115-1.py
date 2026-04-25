
import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and here is _choice2_."

# Data to substitute
data1 = "variable1"
data2 = "variable2"

# Using re.sub and formatting
plot = re.sub(r'_choice1_', '%s' % data1, plot)
plot = re.sub(r'_choice2_', '%s' % data2, plot)

print(plot)
