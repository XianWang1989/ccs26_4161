
import re

# Sample data and plot string
data1 = "First Choice"
data2 = "Second Choice"
plot = "This is a test with _choice1_ and _choice2_. Another occurrence of _choice1_."

# Substitute using re.sub and format string
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the final string with all occurrences replaced
result = plot % (data1, data2)

print(result)
