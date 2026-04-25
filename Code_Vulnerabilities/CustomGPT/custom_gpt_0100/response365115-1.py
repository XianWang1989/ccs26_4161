
import re

# Sample data
plot = "This is a _choice1_ and here is another _choice1_. Then there's a _choice2_ here."
data1 = "first choice"
data2 = "second choice"

# Substitute all occurrences
plot = re.sub(r'_choice1_', '%s', plot) % (data1, data1)
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)
