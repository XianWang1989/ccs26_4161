
msg = input("Message? ")
length = len(msg)
output = []

for i in range(0, length, 3):
    output.append(msg[i])

# Join the list into a single string with spaces
result = " ".join(output)
print(result)
