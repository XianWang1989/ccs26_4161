
import re

# Example data
plot = "This is a _choice1_ and another _choice1_ along with _choice2_."
data1 = "first choice"
data2 = "second choice"

# Substitute variables using re.sub
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Use % formatting only once at the end
plot = plot % (data1, data2)

print(plot)
