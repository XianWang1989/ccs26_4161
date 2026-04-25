
import re

# Sample data
data = {'choice1': "first_choice", 'choice2': "second_choice"}

# Example plot string with placeholders
plot = "This is a {choice1} and here is another {choice1}. Also, don't forget {choice2}!"

# Using str.format for substitution
formatted_plot = plot.format(**data)

print(formatted_plot)
