
import re

# Sample data
plot = "This is a _choice1_ test with _choice2_ and _choice1_ again."
data1 = "first choice"
data2 = "second choice"

# Use a tuple for all replacements
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the final string with the data
plot = plot % (data1, data2)

print(plot)
