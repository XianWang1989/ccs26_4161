
msg = input("Message? ")
length = len(msg)
result = []  # Create a list to store every third character

# Collect every third character
for i in range(0, length, 3):
    result.append(msg[i])

# Join the characters with a space and print the result
output = " ".join(result)
print(output)
