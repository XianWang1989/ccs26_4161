
import re

# Sample string
plot = "This is a _choice1_ and here is another _choice1_. Now we have _choice2_ too."

# Data to substitute
data1 = "first choice"
data2 = "second choice"

# Perform substitutions
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)
