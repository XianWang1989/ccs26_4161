
import re

# Sample plot string with multiple occurrences
plot = "This is a _choice1_ string with _choice1_ and _choice2_ occurrences."

# Data to substitute
data1 = "first choice"
data2 = "second choice"

# Use re.sub to substitute placeholders
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)
