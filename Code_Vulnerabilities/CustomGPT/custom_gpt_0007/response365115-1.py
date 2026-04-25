
import re

# Sample data and placeholders
plot = "This is a _choice1_ and that is a _choice2_ and again a _choice1_."
data = {
    '_choice1_': 'apple',
    '_choice2_': 'banana'
}

# Function to replace all occurrences
def substitute_variables(plot, substitutions):
    for key, value in substitutions.items():
        plot = re.sub(re.escape(key), value, plot)
    return plot

# Perform substitution
plot = substitute_variables(plot, data)

print(plot)
