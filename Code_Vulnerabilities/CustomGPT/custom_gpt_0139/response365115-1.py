
import re

# Sample string with multiple occurrences
plot = "This is a _choice1_ and this is another _choice1_ with a _choice2_."

# Sample data to substitute
data1 = "VALUE1"
data2 = "VALUE2"

# Perform substitutions
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)
