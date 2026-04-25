
import re

# Sample input string
plot = "This is a _choice1_ and another _choice1_. Additionally, here is a _choice2_."

# Data to substitute for the placeholders.
data1 = "FIRST_CHOICE"
data2 = "SECOND_CHOICE"

# Use re.sub and format to replace placeholders dynamically.
plot = re.sub(r'_choice1_', '{}', plot)
plot = re.sub(r'_choice2_', '{}', plot)

# Format the string with the data
plot = plot.format(data1, data2)

# Print the modified string.
print(plot)
