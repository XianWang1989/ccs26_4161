
import re

# Sample plot string
plot = "_choice1_ and _choice2_ are options from _choice1_"

# Data to substitute
data1 = "Option A"
data2 = "Option B"

# Substitute using a single pass with a callback function
def substitute_choices(match):
    choice = match.group(0)
    if choice == "_choice1_":
        return data1
    elif choice == "_choice2_":
        return data2
    return choice

# Perform the substitution
plot = re.sub(r'_choice1_|_choice2_', substitute_choices, plot)

print(plot)
