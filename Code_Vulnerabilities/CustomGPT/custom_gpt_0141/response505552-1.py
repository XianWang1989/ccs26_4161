
msg = input("Message? ")
length = len(msg)

# Create a list to hold every third character
result = []

# Iterate through the string and collect every third character
for i in range(0, length, 3):
    result.append(msg[i])

# Join the list with spaces and print the result
output = " ".join(result)
print(output)
