
import re

# Sample data
data1 = "first_choice"
data2 = "second_choice"

# Example plot string with multiple occurrences
plot = "This is a _choice1_ and here is another _choice1_. Also, don't forget _choice2_!"

# Using re.sub to replace placeholders with formatted strings
plot = plot.replace('_choice1_', '%s')  # Replace all occurrences with a placeholder
plot = plot.replace('_choice2_', '%s')  # Replace all occurrences with a placeholder

# Performing the substitution using str.format
plot = plot % (data1, data2)

print(plot)
