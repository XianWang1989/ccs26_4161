
import re

# Sample data
plot = "This is a _choice1_ and here is another _choice1_. Also, check _choice2_."
data1 = "apple"
data2 = "banana"

# A function to use in re.sub that formats with the appropriate data
def substitute_choice(match):
    choice = match.group(0)  # Get the matched pattern
    if choice == '_choice1_':
        return data1  # return data1 for _choice1_
    elif choice == '_choice2_':
        return data2  # return data2 for _choice2_

# Perform the substitution
plot = re.sub(r'_choice1_|_choice2_', substitute_choice, plot)

print(plot)
