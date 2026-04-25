
msg = input("Message? ")
length = len(msg)
result = []  # Create a list to hold every third character

for i in range(0, length, 3):
    x = msg[i]
    result.append(x)  # Append the character to the list

# Join the list with spaces and print the result
output = " ".join(result)
print(output)
