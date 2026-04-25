
# Using a single re.sub with a custom function to format the replacements
def substitute_choices(plot, data1, data2):
    plot = re.sub(r'_choice1_', data1, plot)
    plot = re.sub(r'_choice2_', data2, plot)
    return plot

# Call the function
plot = substitute_choices(plot, data1, data2)
print(plot)
