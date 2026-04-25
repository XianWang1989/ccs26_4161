
import re

# Sample data
plot = "This is a _choice1_ example with _choice2_ and another _choice1_."
data1 = "first choice"
data2 = "second choice"

# Use re.sub to substitute each variable
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format the string with your data
plot = plot % (data1, data2)

print(plot)
