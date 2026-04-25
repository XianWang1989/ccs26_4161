
import re

# Sample data
plot = "This is a _choice1_ and here is another _choice1_. Also, _choice2_ is here."
data1 = "first choice"
data2 = "second choice"

# Replace placeholders with formatted string
formatted_plot = plot.replace('_choice1_', '%s').replace('_choice2_', '%s')
plot_final = formatted_plot % (data1, data2)

print(plot_final)
