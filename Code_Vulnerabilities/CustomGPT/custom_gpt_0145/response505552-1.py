
msg = input("Message? ")
length = len(msg)
output = []  # Create an empty list to hold every third letter

for i in range(0, length, 3):
    output.append(msg[i])  # Append the third letter to the list

# Join the list items with a space and print them
print(" ".join(output))
