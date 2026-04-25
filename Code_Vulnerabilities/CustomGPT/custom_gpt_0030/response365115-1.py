
import re

# Sample plot string with placeholders
plot = "This is a _choice1_ and here is another _choice1_. Also, we have _choice2_."

# Data to substitute
data = {
    'choice1': 'apple',
    'choice2': 'banana'
}

# Function to substitute placeholders
def substitute_choices(plot, data):
    # Replace placeholders using a dictionary
    for key, value in data.items():
        plot = re.sub(rf'_{key}_', value, plot)
    return plot

# Performing the substitution
new_plot = substitute_choices(plot, data)

print(new_plot)
