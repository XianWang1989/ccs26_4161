
msg = input("Message? ")
length = len(msg)
result = []  # Create a list to hold the letters

for i in range(0, length, 3):
    result.append(msg[i])  # Append every third letter

# Join the list with spaces and print the result
output = " ".join(result)
print(output)
