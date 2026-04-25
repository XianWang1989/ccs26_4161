
import re

data1 = "First Choice"
data2 = "Second Choice"
plot = "This is a _choice1_ and this is a _choice2_. _choice1_ again."

# Substitute placeholders using a function
def substitute(match):
    if match.group(0) == '_choice1_':
        return data1
    elif match.group(0) == '_choice2_':
        return data2

plot = re.sub(r'_choice1_|_choice2_', substitute, plot)

print(plot)
