
import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and here is _choice2_."

# Data to substitute
data1 = "variable1"
data2 = "variable2"

# Using format
plot = plot.replace('_choice1_', data1)
plot = plot.replace('_choice2_', data2)

print(plot)
