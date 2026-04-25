
import re

data1 = 'first_value'
data2 = 'second_value'
plot = "Here is _choice1_ and here is _choice2_ and again _choice1_."

# Define a function to handle substitutions
def substitute(match):
    if match.group(0) == '_choice1_':
        return '%s' % data1
    elif match.group(0) == '_choice2_':
        return '%s' % data2

# Use re.sub with the substitution function
plot = re.sub(r'(_choice1_|_choice2_)', substitute, plot)

print(plot)  # This will output: Here is first_value and here is second_value and again first_value.
