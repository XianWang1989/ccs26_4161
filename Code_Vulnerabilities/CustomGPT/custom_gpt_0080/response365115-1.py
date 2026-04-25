
import re

# Sample data
plot = "_choice1_ is chosen, and _choice2_ is also selected."
data1 = "Option A"
data2 = "Option B"

# Substitute occurrences
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)
