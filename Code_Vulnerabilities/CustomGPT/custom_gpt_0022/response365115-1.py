
import re

# Sample input data
plot = "This is _choice1_ and here is _choice2_. Also _choice1_ again."
data1 = "apple"
data2 = "banana"

# Substitute using re.sub and format
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)
