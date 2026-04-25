
import re

# Example data
data1 = "First Choice"
data2 = "Second Choice"
plot = "This is a _choice1_ and that is a _choice2_. _choice1_ again."

# Substitute in one go
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)
