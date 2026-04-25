
import re

# Example data
data = {
    '_choice1_': 'option1',
    '_choice2_': 'option2'
}

# Sample plot string
plot = "This is a _choice1_ and that is a _choice2_. Also, _choice1_ again."

# Function to substitute based on dictionary
def substitute_choices(plot, data):
    for key, value in data.items():
        plot = re.sub(re.escape(key), value, plot)
    return plot

# Call the function
result = substitute_choices(plot, data)
print(result)
