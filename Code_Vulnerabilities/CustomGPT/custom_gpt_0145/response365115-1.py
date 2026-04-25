
import re

# Your example data
data1 = "FirstChoice"
data2 = "SecondChoice"
plot = "_choice1_ some text _choice2_ more text _choice1_"

# Substitute using a function to handle multiple occurrences
def substitute_choices(match):
    if match.group(0) == '_choice1_':
        return data1
    elif match.group(0) == '_choice2_':
        return data2

plot = re.sub(r'_choice1_|_choice2_', substitute_choices, plot)

print(plot)
