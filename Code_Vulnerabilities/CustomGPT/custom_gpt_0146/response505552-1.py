
msg = input("Message? ")
length = len(msg)
result = []  # Initialize an empty list to collect characters

for i in range(0, length, 3):
    result.append(msg[i])  # Add every third character to the list

# Join the collected characters with a space and print them
print(" ".join(result))
