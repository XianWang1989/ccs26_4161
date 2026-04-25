
import re

# Sample data and plot string
data1 = "value1"
data2 = "value2"
plot = "This is a _choice1_ and another _choice1_ with _choice2_."

# Substitute placeholders with %s
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Using str.format to fill in the values
plot = plot.format(data1, data2)

print(plot)
