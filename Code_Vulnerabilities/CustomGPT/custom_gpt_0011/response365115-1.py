
import re

# Sample data
plot = "This is _choice1_ and this is _choice1_ again. Here's a different choice: _choice2_."
data1 = "Option A"
data2 = "Option B"

# Substitute using two passes
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)
