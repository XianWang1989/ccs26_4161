
import re

# Sample input string with multiple occurrences of each placeholder.
plot = "This is a _choice1_ and another _choice1_. Additionally, here is a _choice2_."

# Data to substitute for the placeholders.
data1 = "FIRST_CHOICE"
data2 = "SECOND_CHOICE"

# Use re.sub to replace the placeholders with the corresponding values.
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

# Print the modified string.
print(plot)
