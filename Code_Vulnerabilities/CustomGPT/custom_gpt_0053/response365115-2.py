
plot = "This is a test with {choice1} and {choice2} and {choice1} again."

# Substitute with format placeholders
result = plot.format(choice1=data1, choice2=data2)

print(result)  # Output: This is a test with Apple and Banana and Apple again.
