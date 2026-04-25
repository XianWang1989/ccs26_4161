
import re

# Example data
plot = "This is a _choice1_ and here is another _choice1_ and a _choice2_."
data1 = "option1"
data2 = "option2"

# Substitute multiple occurrences
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)
