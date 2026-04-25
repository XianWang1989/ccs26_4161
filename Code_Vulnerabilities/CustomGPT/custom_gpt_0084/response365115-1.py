
import re

# Example data
data1 = 'option1'
data2 = 'option2'
plot = 'This is a _choice1_ and another _choice1_. Also, here is _choice2_.'

# Substitute all occurrences of _choice1_ and _choice2_
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)
