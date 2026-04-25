
import re

# Sample data
plot = "This is a plot with _choice1_ and _choice2_."
data1 = "first_choice"
data2 = "second_choice"

# Substitute placeholders with values
plot = re.sub(r'_choice1_', '%s', plot) % data1
plot = re.sub(r'_choice2_', '%s', plot) % data2

print(plot)  # Output: This is a plot with first_choice and second_choice.
