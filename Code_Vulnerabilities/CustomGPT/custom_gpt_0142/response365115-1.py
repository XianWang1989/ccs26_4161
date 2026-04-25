
import re

# Dummy data for demonstration
plot = "This is a _choice1_ and here is another _choice1_. Also _choice2_ appears here."
data1 = "First Choice"
data2 = "Second Choice"

# Substitute all occurrences using the provided data
plot = re.sub(r'_choice1_', data1, plot)  # Substitute for _choice1_
plot = re.sub(r'_choice2_', data2, plot)  # Substitute for _choice2_

print(plot)
