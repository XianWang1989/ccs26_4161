
import re

# Sample data and plot string
data1 = "first_choice"
data2 = "second_choice"
plot = "This is _choice1_ and also _choice1_ and _choice2_."

# Substitute occurrences
plot = re.sub(r'_choice1_', data1, plot)
plot = re.sub(r'_choice2_', data2, plot)

print(plot)
