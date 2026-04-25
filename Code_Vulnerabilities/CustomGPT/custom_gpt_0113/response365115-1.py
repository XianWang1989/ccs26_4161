
import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and another _choice2_. And again _choice1_."

# Data for substitution
data1 = "option1"
data2 = "option2"

# Replace placeholders securely
plot = plot.replace('_choice1_', '{}').replace('_choice2_', '{}').format(data1, data2)

print(plot)
