
msg = input("Message? ")
length = len(msg)
result = []  # Create an empty list to store the characters

for i in range(0, length, 3):
    result.append(msg[i])  # Add the character to the list

# Join the list into a string with spaces and print it
print(" ".join(result))
