
import re

# Sample plot string
plot = "This is a test with _choice1_ and another _choice1_ and _choice2_."

# Sample data for substitution
data1 = "first_choice"
data2 = "second_choice"

# Substitute occurrences
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

# Print the final result
print(plot)
