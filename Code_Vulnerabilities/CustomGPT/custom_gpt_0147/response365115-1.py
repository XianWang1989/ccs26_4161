
import re

# Sample data and plot string
data1 = "First Choice"
data2 = "Second Choice"
plot = "This is a plot with _choice1_ and _choice1_ again, and here is _choice2_."

# Use a single regular expression to substitute and format all occurrences at once
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Now format the string with all data
plot = plot % (data1, data2)

print(plot)
