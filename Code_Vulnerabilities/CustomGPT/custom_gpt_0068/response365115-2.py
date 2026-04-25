
# Using named placeholders
plot = "This is a {choice1} and another {choice1}. Also, this is a {choice2}."

# Format with data
formatted_plot = plot.format(choice1=data1, choice2=data2)

print(formatted_plot)
