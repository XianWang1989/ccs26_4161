
import re

data1 = "Option A"
data2 = "Option B"
plot = "_choice1_ and then _choice2_ again. _choice1_ here too."

# Substitute all occurrences
plot = re.sub(r'_choice1_', '%s' % data1, plot)
plot = re.sub(r'_choice2_', '%s' % data2, plot)

print(plot)
