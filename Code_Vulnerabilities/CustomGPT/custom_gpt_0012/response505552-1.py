
msg = input("Message? ")
length = len(msg)
output = []  # List to hold every third character

# Loop through every third character
for i in range(0, length, 3):
    output.append(msg[i])  # Add the character to the list

# Join the list into a string with spaces and print
print(" ".join(output))
