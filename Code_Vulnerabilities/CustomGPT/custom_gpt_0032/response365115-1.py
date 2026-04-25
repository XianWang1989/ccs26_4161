
import re

# Example input string
plot = "This is a test: _choice1_ and _choice2_ and _choice1_ again."

# Sample data for substitution
data1 = "first choice"
data2 = "second choice"

# Perform substitutions using formatted string
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)
