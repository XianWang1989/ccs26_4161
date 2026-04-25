
msg = input("Message? ")
length = len(msg)
result = []  # Create a list to hold the selected characters

# Iterate through the message string
for i in range(0, length, 3):
    result.append(msg[i])  # Add every third letter to the result list

# Use join to create a string with spaces in between and print it
print(" ".join(result))
