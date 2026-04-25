
msg = input("Message? ")
output = []  # Initialize an empty list to gather every third letter

length = len(msg)
for i in range(0, length, 3):
    output.append(msg[i])  # Add the letter to the list

# Join the list into a string with spaces and print it
print(" ".join(output))
