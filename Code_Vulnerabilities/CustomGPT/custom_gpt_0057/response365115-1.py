
import re

def substitute_choices(plot, data1, data2):
    plot = re.sub(r'_choice1_', '%s', plot)
    plot = re.sub(r'_choice2_', '%s', plot)
    formatted_plot = plot % (data1, data2)
    return formatted_plot

# Example usage
plot_template = "This is a _choice1_ and that is a _choice2_."
data1 = "dog"
data2 = "cat"

result = substitute_choices(plot_template, data1, data2)
print(result)
