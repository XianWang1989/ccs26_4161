
msg = input("Message? ")
output = []  # Create an empty list to store the letters

for i in range(0, len(msg), 3):
    output.append(msg[i])  # Add every third letter to the list

# Join the letters with a space and print the result
result = " ".join(output)
print(result)
