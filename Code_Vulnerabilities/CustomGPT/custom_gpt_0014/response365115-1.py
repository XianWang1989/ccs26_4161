
import re

# Example data
plot = "This is a _choice1_ and another _choice1_ and also _choice2_."
data1 = "first choice"
data2 = "second choice"

# Use re.sub with a format function
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Format with data
plot = plot % (data1, data2)

# Output the final string
print(plot)
