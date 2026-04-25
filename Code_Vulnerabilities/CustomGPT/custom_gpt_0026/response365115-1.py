
import re

# Sample input string
plot = "This is a _choice1_ and that is a _choice2_. Also, _choice1_ appears again."

# Variables to substitute
data1 = "apple"
data2 = "banana"

# Substitute placeholders with `%s` and format afterwards
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the string with the data
plot = plot % (data1, data2)

print(plot)
