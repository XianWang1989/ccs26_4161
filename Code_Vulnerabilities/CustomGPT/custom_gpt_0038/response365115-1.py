
import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and that is a _choice2_. _choice1_ is fun!"

# Data for substitution
data = {
    '_choice1_': 'apple',
    '_choice2_': 'orange'
}

# Function to replace placeholders using the dictionary
def substitute_placeholders(plot, data):
    for key, value in data.items():
        plot = re.sub(re.escape(key), value, plot)
    return plot

# Perform the substitution
result = substitute_placeholders(plot, data)
print(result)  # Output: This is a apple and that is a orange. apple is fun!
