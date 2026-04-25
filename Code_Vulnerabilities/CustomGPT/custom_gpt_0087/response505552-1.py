
msg = input("Message? ")
output = []

# Read every third letter and store it in the output list
for i in range(0, len(msg), 3):
    output.append(msg[i])

# Print the result with spaces in between
print(" ".join(output))
