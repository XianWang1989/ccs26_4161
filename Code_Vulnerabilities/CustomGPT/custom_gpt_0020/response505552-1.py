
msg = input("Message? ")
length = len(msg)

# Use a list to collect every third character
characters = []
for i in range(0, length, 3):
    characters.append(msg[i])

# Join the characters with a space and print
output = " ".join(characters)
print(output)
