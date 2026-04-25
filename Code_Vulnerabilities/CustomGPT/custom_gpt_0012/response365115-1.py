
import re

# Example data
data1 = "Apple"
data2 = "Banana"
plot = "This is a _choice1_ and that is a _choice2_. We have _choice1_ again."

# Substitute variables safely
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)
