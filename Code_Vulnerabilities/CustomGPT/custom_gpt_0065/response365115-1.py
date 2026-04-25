
import re

# Sample plot string
plot = "This is a _choice1_ and this is another _choice1_ and _choice2_."

# Data to substitute
data1 = "first choice"
data2 = "second choice"

# Using re.sub to substitute and format
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

# Print the result
print(plot)
