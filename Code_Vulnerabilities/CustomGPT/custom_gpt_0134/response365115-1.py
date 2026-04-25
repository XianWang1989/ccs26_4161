
import re

# Example plot string with placeholders
plot = "This is a _choice1_ and here is another _choice2_"

# Data to substitute into the placeholders
data1 = "apple"
data2 = "banana"

# Substitute using re.sub and format
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Format the final string with the data
plot = plot.format(data1, data2)

print(plot)
