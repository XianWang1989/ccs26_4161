
import re

# Sample data
data1 = "foo"
data2 = "bar"
plot = "This is _choice1_ and _choice2_. Also, _choice1_ again."

# Substitute using a single pass with placeholders
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use the % operator for string formatting
formatted_plot = plot % (data1, data2)

print(formatted_plot)
