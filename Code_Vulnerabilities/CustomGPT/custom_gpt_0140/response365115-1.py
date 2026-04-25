
import re

# Sample data
plot = "This is a _choice1_ and this is also a _choice1_. But here is a _choice2_."
data1 = "first choice"
data2 = "second choice"

# Substitute multiple occurrences
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)
