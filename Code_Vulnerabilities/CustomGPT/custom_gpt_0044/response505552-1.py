
msg = input("Message? ")
output = []  # Create an empty list to store each character

# Read every third character
for i in range(0, len(msg), 3):
    output.append(msg[i])  # Append the character to the list

# Join the characters with a space and print
print(" ".join(output))
