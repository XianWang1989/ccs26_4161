
import re

# Sample plot string with multiple placeholders
plot = "This is a _choice1_ and another _choice1_. Also, here is _choice2_."

# Data to substitute
data1 = "option A"
data2 = "option B"

# Substitute using re.sub
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)
