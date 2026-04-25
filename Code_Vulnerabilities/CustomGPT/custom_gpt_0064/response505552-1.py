
msg = input("Message? ")
length = len(msg)
output = []

for i in range(0, length, 3):
    output.append(msg[i])

# Join the characters with spaces and print the result
result = " ".join(output)
print(result)
