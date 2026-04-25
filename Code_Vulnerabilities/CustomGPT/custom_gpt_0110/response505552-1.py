
msg = input("Message? ")
length = len(msg)
result = []

for i in range(0, length, 3):
    result.append(msg[i])

# Join the list with spaces and print the result
output = " ".join(result)
print(output)
