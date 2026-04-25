
import re

# Sample data
data1 = "Substitution1"
data2 = "Substitution2"
plot = "Here is _choice1_ and here is _choice2_ as well as _choice1_ again"

# Use re.sub to replace placeholders and use format to inject values
plot = re.sub(r'_choice1_', '%s', plot)
plot = re.sub(r'_choice2_', '%s', plot)

# Apply formatting
plot = plot % (data1, data2)

print(plot)
